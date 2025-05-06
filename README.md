# n8n Video Summarizer Bot

## Overview
This project is an automated workflow built with n8n that creates AI-generated video summaries from web content. The workflow:

1. Accepts a URL and research topic via Telegram bot command
2. Scrapes the provided webpage and related subpages
3. Generates a concise research summary using Groq LLM
4. Creates a talking avatar video using D-ID API
5. Uploads the video to YouTube
6. Sends the YouTube link back to the user via Telegram

## Features
- **Web Scraping**: Extracts content from multiple pages
- **AI Summarization**: Uses Groq LLM to create concise summaries
- **AI Video Generation**: Creates talking avatar videos using D-ID
- **Automated Publishing**: Direct upload to YouTube
- **User Interaction**: Simple Telegram bot interface

## Prerequisites
- n8n instance
- Telegram Bot API credentials
- D-ID API credentials
- Groq API credentials
- YouTube API credentials

## Setup

### 1. n8n Setup
1. Install n8n using npm:
   ```
   npm install n8n -g
   ```
2. Start n8n:
   ```
   n8n start
   ```

### 2. Import Workflow
1. Navigate to n8n dashboard
2. Go to Workflows → Import From File
3. Select `workflows/summarize_video.json`

### 3. Configure Credentials
Configure the following credentials in n8n:
- Telegram Bot API
- D-ID API
- Groq API
- YouTube API

### 4. Configure Webhook
1. Enable the Telegram Trigger node
2. Set up webhook for your Telegram bot using the provided URL

## Usage
Send a command to your Telegram bot in this format:
```
/research Research Topic
https://example.com/page-to-summarize
```

The bot will:
1. Acknowledge your request
2. Process the webpage
3. Generate a summary
4. Create a video
5. Upload to YouTube
6. Send you the YouTube link

## Architecture
This workflow uses several interconnected n8n nodes:
- Telegram Trigger: Receives commands from users
- HTTP Request: Scrapes web content
- HTML Extract: Parses content from HTML
- Code nodes: Process data between steps
- Groq/LangChain: Generates summaries
- D-ID API: Creates talking avatar videos
- YouTube integration: Uploads videos

See `docs/architecture.md` for detailed architecture information.

## License
[MIT](LICENSE)