# n8n Video Summarizer Bot

An n8n automation that transforms web content into AI‑generated video summaries. This repo hosts two workflows:

1. **Legacy**: Groq LLM + D‑ID API (custom scraping and processing)
2. **Optimized**: Firecrawl Scrape + Google Gemini (streamlined and recommended)

---

## 🚀 Overview

Both workflows follow the same high‑level pipeline:

1. **Telegram Command**: `/research <Topic>\n<URL>`
2. **Scrape**: Fetch markdown (and screenshot) of the page
3. **Summarize**: Generate concise research summary via LLM
4. **Video**: Create talking avatar video
5. **Publish**: Upload to YouTube
6. **Reply**: Send the video link back on Telegram

Use the **Optimized** version for simplicity; the Legacy flow remains available if you need its Groq+DIY scraping approach.

---

## 📁 Repository Structure

```
├── workflows/
│   ├── original_workflow.json       # Legacy Groq + D‑ID version (custom HTTP + HTML extract)
│   └── new_workflow.json            # Optimized Firecrawl + Gemini version
├── docs/
│   └── architecture.md              # Architecture and node-by-node breakdown
└── README.md                        # This file
```

---

## 🔧 Prerequisites

* **n8n** (Cloud or self‑hosted)
* **Telegram Bot** token
* **YouTube** Data API credentials

### Legacy Flow

* **Groq** API credentials
* **D‑ID** API credentials
* (Built‑in HTTP Request + HTML Extract nodes for scraping)

### Optimized Flow

* **Firecrawl** API Key
* **Google Cloud** credentials (Gemini Chat)
* (Optional) **Avatar API** credentials if not using D‑ID

---

## ⚙️ Legacy Workflow (Groq + D‑ID)

1. **Import** `workflows/original_workflow.json`
2. **Configure** credentials: Telegram, Groq, D‑ID, YouTube
3. The workflow uses:

   * **HTTP Request** & **HTML Extract** nodes to scrape the page
   * **Groq LLM** to summarize content
   * **D‑ID API** to generate talking‑avatar video
   * **YouTube Node** to publish
4. **Activate** Telegram Trigger and send `/research` to run.

---

## ⚡️ Optimized Workflow (Firecrawl + Gemini)

1. **Import** `workflows/new_workflow.json`
2. **Configure** credentials: Telegram, Firecrawl, Google Cloud (Gemini), YouTube
3. **Activate** Telegram Trigger
4. **Usage**: Send `/research` and let it run through Firecrawl & Gemini.

### Firecrawl Scrape Node

* **Endpoint**: `POST https://api.firecrawl.dev/v1/scrape`
* **Body** (JSON):

  ```json
  {
    "url": "{{ $json.urlToScrape }}",
    "formats": ["markdown"],
    "onlyMainContent": true
  }
  ```
* **Headers**:

  * `Authorization: Bearer <YOUR_FIRECRAWL_KEY>`
  * `Content-Type: application/json`
* **Output**:

  * `data[0].markdown`: Page content




## 🤝 Contributing

Contributions, bug reports, and feature requests are **welcome**! Feel free to:

* Open issues for bugs or suggestions
* Submit pull requests
* Improve documentation or add new workflows

> **Note:** Third‑party API changes can cause occasional malfunctions. Please report issues so we can address them quickly.

---

## 📜 License

MIT License – see [LICENSE](LICENSE) for details.
