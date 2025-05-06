# Telegram Bot Integration Guide

This guide outlines how to properly set up and configure the Telegram bot that functions as the user interface for the n8n Video Summarizer Bot.

## Prerequisites

1. A Telegram account
2. n8n instance with the workflow installed
3. Public internet access for webhook functionality (or tunneling service)

## Setup Steps

### 1. Create a Telegram Bot

1. Open Telegram and search for "BotFather"
2. Start a conversation with BotFather and send the command `/newbot`
3. Follow the prompts to name your bot and create a username
4. Once created, BotFather will provide an API token - **save this token securely**

### 2. Configure n8n Credentials

1. In n8n, go to **Settings** > **Credentials**
2. Click on **New Credential**
3. Select **Telegram API**
4. Enter the API token provided by BotFather
5. Save the credential with a recognizable name (e.g., "Video Summarizer Bot")

### 3. Configure the Telegram Trigger Node

1. Open the workflow in n8n
2. Select the **Telegram Trigger** node
3. Under credentials, select the Telegram API credential you created
4. Enable "Updates" to be received by the node
5. Save the workflow

### 4. Set Up Webhook

1. Activate the workflow
2. n8n will automatically register the webhook with Telegram
3. Test that the webhook is working by sending a message to your bot

## Usage Commands

The bot responds to the following command format:

```
/research [Topic]
[URL to scrape]
```

Example:
```
/research Climate Change Effects
https://example.com/climate-article
```

## Error Messages

When users send incorrectly formatted commands, they will receive this error message:

```
Invalid command format. Please use:

/research Research Topic
URL to scrape
```

## Response Flow

1. User sends command in correct format
2. Bot immediately acknowledges with: "I'm starting your research and scraping the provided URL. Please wait while I process your request..."
3. After processing is complete, bot sends: "Your video is now available at: [YouTube URL]"

## Troubleshooting

- **Bot Not Responding:** Check that the workflow is active and the webhook is properly registered
- **Webhook Registration Failures:** Ensure your n8n instance is publicly accessible
- **Command Not Recognized:** Verify the exact format of the command, including the space after "/research"

## Security Considerations

- The Telegram bot token grants access to control your bot - keep it secure
- Consider implementing rate limiting if deploying publicly
- Monitor usage to prevent abuse of YouTube and D-ID API quotas