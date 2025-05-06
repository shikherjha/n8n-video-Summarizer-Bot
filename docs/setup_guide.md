# Setup Guide

This guide provides detailed instructions for setting up the Video Summarizer Bot workflow in n8n.

## Prerequisites

Before setting up the workflow, ensure you have:

1. A running n8n instance (v0.214.0 or later recommended)
2. Accounts and API credentials for:
   - Telegram Bot API
   - D-ID API
   - Groq AI API
   - YouTube API

## Installation Steps

### Step 1: Install n8n

If you haven't already installed n8n, you can do so using npm:

```bash
npm install n8n -g
```

Start n8n:

```bash
n8n start
```

This will launch the n8n server, typically accessible at `http://localhost:5678`.

### Step 2: Import the Workflow

1. Download the `summarize_video.json` file from the workflows directory
2. In the n8n dashboard, click on "Workflows" in the side menu
3. Click the "Import from File" button
4. Select the downloaded `summarize_video.json` file
5. Save the imported workflow

### Step 3: Configure API Credentials

#### Telegram Bot Setup

1. In n8n, go to "Credentials" and add a new "Telegram API" credential
2. Obtain a bot token from [@BotFather](https://t.me/botfather) on Telegram
3. Enter the bot token in the credential form
4. Save the credential and assign it to the Telegram nodes in the workflow

#### D-ID API Setup

1. Create an account at [D-ID](https://www.d-id.com/)
2. Generate API key credentials from your D-ID dashboard
3. In n8n, add a new "HTTP Basic Auth" credential
4. Enter your D-ID API key and secret
5. Save and assign to the D-ID API request nodes

#### Groq API Setup

1. Create an account at [Groq](https://console.groq.com/)
2. Generate an API key from your Groq dashboard
3. In n8n, add a new "Groq API" credential
4. Enter your Groq API key
5. Save and assign to the Groq Chat Model node

#### YouTube API Setup

1. Create/use a Google account with access to YouTube
2. Go to the [Google Developer Console](https://console.developers.google.com/)
3. Create a new project and enable the YouTube Data API v3
4. Create OAuth 2.0 credentials
5. In n8n, add a new "YouTube OAuth2 API" credential
6. Complete the OAuth flow to authorize access to your YouTube account
7. Save and assign to the YouTube upload node

### Step 4: Configure Telegram Webhook

1. Enable the Telegram Trigger node in the workflow
2. n8n will generate a webhook URL
3. Set up this webhook URL for your Telegram bot using the Telegram Bot API:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<YOUR_N8N_WEBHOOK_URL>
   ```
   
   > Note: Your n8n instance must be publicly accessible for the webhook to work. You can use a service like ngrok to expose a local n8n instance.

### Step 5: Customize the Workflow (Optional)

You may want to customize:

1. The avatar used in D-ID (modify the source_url in preprocessing_for_did.py)
2. The summarization prompt (modify prompts/summarizer_prompt.txt)
3. The YouTube upload parameters (category, privacy settings, etc.)

### Step 6: Activate the Workflow

1. In the n8n workflow editor, toggle the "Active" switch to enable the workflow
2. The workflow is now ready to receive commands

## Testing the Setup

To test if your setup is working:

1. Send a message to your Telegram bot with the following format:
   ```
   /research Your Research Topic
   https://example.com/page-to-summarize
   ```
2. The bot should acknowledge your request
3. Wait for the workflow to process (this may take a few minutes)
4. You should receive a link to the generated YouTube video

## Troubleshooting

### Common Issues

1. **Telegram webhook not working**
   - Ensure your n8n instance is publicly accessible
   - Verify the webhook was set correctly with: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo`

2. **D-ID API errors**
   - Check your API credentials
   - Ensure your account has sufficient credits
   - Verify the request format in the preprocessing_for_did.py script

3. **YouTube upload fails**
   - Confirm your OAuth credentials are valid and not expired
   - Ensure you have proper permissions to upload to the YouTube account
   - Check if the video file was created correctly

4. **Web scraping not working**
   - Some websites block scraping; try with a different website
   - Add user-agent headers to the HTTP Request node if needed
   - Check if content selectors in HTML Extract nodes need adjustment