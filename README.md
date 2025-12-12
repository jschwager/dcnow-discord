
# Dreamcast Now! Discord bot

A Python script that integrates with monitors [Dreamcast Now!](https://dreamcast.online/now/) for newly logged on users and posts them to a Discord channel using a webhook.

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

2. Add an entry (example: run every 30 minutes):
    ```cron
    */30 * * * * /usr/bin/python3 /path/to/dcnow-discord/main.py
    ```

3. Common cron patterns:
    - `0 * * * *` - Every hour
    - `0 9 * * *` - Daily at 9 AM
    - `*/15 * * * *` - Every 15 minutes
