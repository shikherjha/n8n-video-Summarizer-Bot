# Video Summarizer Bot Architecture

This document describes the architecture of the n8n-based video summarizer bot workflow.

## Overview

The workflow is organized as a sequential pipeline that processes web content into a summarized video. It consists of the following high-level stages:

1. **User Interaction** - Telegram bot interface
2. **Content Acquisition** - Web scraping
3. **Content Processing** - Text extraction and preparation
4. **Summary Generation** - AI-powered summarization
5. **Video Generation** - Creating a talking avatar video
6. **Publishing** - Uploading to YouTube
7. **Notification** - Sending results back to the user

## Architecture Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │             │     │             │     │             │
│  Telegram   │────▶│ Web Scraper │────▶│ Content     │────▶│ Groq LLM    │
│  Bot        │     │             │     │ Processor   │     │             │
│             │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                  │
                                                                  ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │             │     │             │     │             │
│  Telegram   │◀────│ YouTube     │◀────│ Video       │◀────│ D-ID API    │
│  Notification│     │ Uploader   │     │ Generator   │     │             │
│             │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## Detailed Component Description

### 1. Telegram Bot (Input)
- **Purpose**: Interface with users
- **Components**:
  - Telegram Trigger: Listens for commands in the format `/research [topic] [url]`
  - Command Validator: Ensures proper command format
  - Parameter Extractor: Extracts research topic and URL

### 2. Web Scraper
- **Purpose**: Extract content from the provided URL and related pages
- **Components**:
  - HTTP Request: Fetches the main webpage
  - HTML Extract: Extracts links and content
  - URL Processor: Normalizes links for subpage extraction
  - Batching: Processes links in manageable batches

### 3. Content Processor
- **Purpose**: Organize and prepare the extracted content
- **Components**:
  - Content Merger: Combines content from various pages
  - Context Preparation: Formats data for LLM processing
  - Metadata Preservation: Maintains workflow context

### 4. LLM Summarization
- **Purpose**: Generate concise, accurate summaries
- **Components**:
  - Groq Chat Model: Provides the AI language model
  - Chain LLM: Processes the prompt with content
  - Summary Formatter: Prepares summary for video generation

### 5. D-ID Video Generation
- **Purpose**: Create a talking avatar video
- **Components**:
  - D-ID API Formatter: Prepares the API request
  - Video Creation: Sends the request to D-ID
  - Status Polling: Monitors video creation progress
  - Video Download: Retrieves the completed video

### 6. YouTube Publisher
- **Purpose**: Make the video publicly available
- **Components**:
  - File Preparation: Formats the video for uploading
  - YouTube API: Handles the upload process
  - Link Extractor: Extracts the final video URL

### 7. Telegram Notification (Output)
- **Purpose**: Notify the user of completion
- **Components**:
  - Message Formatter: Creates a user-friendly message
  - Telegram Sender: Delivers the message with video link

## Data Flow

1. User sends command: `/research [topic] [url]`
2. Workflow validates command and acknowledges receipt
3. Main URL is scraped for content and sublinks
4. Sublinks are processed to gather additional relevant content
5. Content is merged and prepared for the LLM
6. LLM generates a concise summary
7. Summary is sent to D-ID API to create a talking avatar video
8. Video generation status is polled until complete
9. Completed video is downloaded
10. Video is uploaded to YouTube
11. YouTube link is sent back to the user via Telegram

## Error Handling

The workflow includes several error handling mechanisms:
- Command validation with error messaging
- HTTP request error handling for web scraping
- Retry logic for D-ID API calls
- Wait nodes for proper API rate limiting

## External Dependencies

The workflow relies on the following external services:
- Telegram Bot API
- Groq AI API
- D-ID API
- YouTube API