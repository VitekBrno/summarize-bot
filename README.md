# Discord Channel Summarizer Bot

A Discord bot that uses Google's Generative AI to summarize channel conversations.

## Features

- Summarize channel messages using Google's Gemini AI
- Configurable message limit
- Easy to use commands

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a Discord bot and get your token:
   - Go to https://discord.com/developers/applications
   - Create a new application
   - Go to the Bot section
   - Create a bot and copy the token
   - Enable Message Content Intent in the Bot section

3. Get your Google AI API key:
   - Go to https://makersuite.google.com/app/apikey
   - Create a new API key

4. Configure the bot:
   - Add your Discord bot token to the `.env` file
   - Add your Google AI API key to the `.env` file

5. Run the bot:
   ```bash
   python bot-summarizer.py
   ```

## Commands

Basic Commands:
- `!sum [number]` - Summarize the last [number] messages (default: 100)
- `!help_summary` - Show help information

Advanced Options:
1. Time-based summary:
   - `!sum 24h` - Summarize messages from last 24 hours
   - `!sum 7d` - Summarize messages from last 7 days

2. User-specific summary:
   - `!sum @username` - Summarize messages mentioning specific user

3. Date range summary:
   - `!sum --after 2024-02-01 --before 2024-02-28` - Summarize messages between dates

## Examples

```
# Basic usage
!sum 50                    # Last 50 messages

# Time-based summaries
!sum 24h                   # Last 24 hours
!sum 7d                    # Last 7 days

# User-specific summaries
!sum @username            # Messages mentioning user
!sum 24h @username       # User mentions in last 24 hours

# Date range summaries
!sum --after 2024-02-01 --before 2024-02-28    # Messages between dates
!sum 7d --after 2024-01-01                     # Last 7 days after Jan 1, 2024
```

## Notes

- The bot uses Google's Gemini Pro model for text generation
- The bot requires the Message Content Intent to be enabled in the Discord Developer Portal