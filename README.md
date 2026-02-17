
# Dreamcast Now! Discord bot

A Python script that integrates with and monitors [Dreamcast Now](https://dreamcast.online/now/) for newly logged on users and posts them to a Discord channel using a webhook.

## Installation

1. Clone the repository and navigate to the project directory.
```bash
git clone https://github.com/jschwager/dcnow-discord.git
cd dcnow-discord
```
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```
**NOTE:** You may need to use the ```--break-system-packages``` option if you receive a message regarding the environment being externally managed.

## Configuration

Edit the `config.ini` file in the project root and configure the Discord webhook URL. [Learn how to create a webhook](https://support.discord.com/hc/en-us/articles/228383668).

If desired, you can configure the **debug** option to ```True``` if you wish to test the script without posting any messages to Discord. 

## Running the Script

Execute the script manually:

```bash
python main.py
```

## Scheduling with Cron

To run this script automatically on a schedule, use cron:

1. Open your crontab editor:
    ```bash
    crontab -e
    ```

2. Add an entry (example: run every 5 minutes):
    ```cron
    */5 * * * * cd /home/pi/dcnow-discord && python3 main.py >> app.log 2>&1
    ```

3. Common cron patterns:
    - `0 * * * *` - Every hour
    - `0 9 * * *` - Daily at 9 AM
    - `*/15 * * * *` - Every 15 minutes
