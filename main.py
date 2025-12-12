import configparser
import json
import requests
from discord_webhook import DiscordWebhook

# Load config from config.ini
config = configparser.ConfigParser()
config.read("config.ini")
debug = config.getboolean("general", "debug")
discord_webhook_url = config.get("discord", "webhook_url")

# Fetch data from DCNow API
response = requests.get("https://dreamcast.online/now/api/users.json")
response.raise_for_status()
new_users_data = response.json()

# Function: Compares new user data with old data from local file
def compare_users():
    try:
        with open("users.json", "r") as local_file:
            old_users_data = json.load(local_file)
    except FileNotFoundError:
        print("No local backup found.")
        return
    
    # Extract users list from the response
    old_users_list = old_users_data if isinstance(old_users_data, list) else old_users_data.get("users", [])
    new_users_list = new_users_data if isinstance(new_users_data, list) else new_users_data.get("users", [])
    
    if new_users_list != old_users_list:
        print("User data has changed!")
        
        # Extract usernames from old data for comparison
        old_usernames = {user["username"] for user in old_users_list}
        
        # Find new users
        new_users = [user for user in new_users_list if user["username"] not in old_usernames]
        
        # DEBUG: Print old users and new users
        if debug == True:
            print(f"Old users: {old_usernames}")
            new_usernames = {user["username"] for user in new_users_list}
            print(f"New users: {new_usernames}")

        if new_users:
            print("New users online:")
            message_content = "New users detected:\n"
            for user in new_users:
                username = user['username']
                last_game_desc = user.get('last_game', {}).get('description', 'N/A')
                message_content += f"- **{username}**: {last_game_desc}\n"
                print(f"- {username}: {last_game_desc}")

            # Post to Discord, show example message in debug mode
            if debug == True:
                print("This is what would have been posted to Discord:")
                print(message_content)
            else:
                print("Posting update to Discord...")
                webhook = DiscordWebhook(url=discord_webhook_url, content=message_content)
                webhook.execute()
    else:
        print("No changes detected.")

def store_users():
    # Store fetched data in local file    
    with open("users.json", "w") as local_file:
        json.dump(new_users_data, local_file)
    print("Successfully stored users data locally as users.json")

# Main execution
if __name__ == "__main__":
    compare_users()
    # Store new data only if not in debug mode
    if debug == False:
        store_users()