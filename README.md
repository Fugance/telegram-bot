# Telegram Moderation Bot

## Overview
This Telegram bot is designed to facilitate the moderation of content submissions within a Telegram channel. It allows users to submit text, images, videos, and GIFs, which are then reviewed by an administrator before being published to the channel. The bot ensures that all submissions are reviewed for appropriateness and relevance before being shared with a broader audience.

## Features
- **Content Submission**: Users can send text, photos, videos, and GIFs to the bot.
- **Admin Review**: Submissions are forwarded to an admin for approval or rejection.
- **Support for Various Media Types**: The bot handles different types of media including text, images, videos, and GIFs.
- **Automatic Posting**: Upon approval, content is automatically posted to the specified Telegram channel.
- **Rejection Notifications**: Users receive notifications if their submissions are rejected.

## Installation

### Prerequisites
- Python 3.6 or higher
- `pip` for package installation
- A Telegram bot token (obtainable through BotFather on Telegram)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fugance/telegram-bot.git
   cd telegram-bot
   ```

2. **Install required packages:**
   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Configure the bot:**
   Edit the `bot_config.py` file to include your `TOKEN`, `ADMIN_ID`, and `CHANNEL_ID`.

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## Usage
- **Start the Bot**: Send `/start` to the bot on Telegram.
- **Submit Content**: Directly send text messages, images, videos, or GIFs to the bot.
- **Admin Review**: The admin receives the submissions with options to approve or reject.
- **Check Channel**: Approved content is automatically posted to the specified channel.

## Configuration
- **TOKEN**: Your bot's unique authentication token.
- **ADMIN_ID**: The Telegram user ID of the administrator.
- **CHANNEL_ID**: The ID of the Telegram channel where approved messages will be posted.
