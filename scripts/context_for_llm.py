"""
Context Preparation for LLM

This script prepares the scraped content for processing by the LLM,
organizing content from multiple sources and maintaining metadata.
"""

def prepare_context_for_llm(items):
    """
    Prepare context for the LLM by organizing scraped content and preserving metadata.
    
    Args:
        items: n8n items array containing scraped content and metadata
        
    Returns:
        List containing a single item with organized content and metadata
    """
    # Collect content from each extracted page
    collected_content = []
    for item in items:
        if item["json"].get("content"):
            collected_content.append({
                "content": item["json"]["content"],
                "url": item["json"].get("url", "")
            })

    # Get the research topic and URL from the first item
    research_topic = items[0]["json"].get("researchTopic", "")
    url_to_scrape = items[0]["json"].get("OriginalUrl", "")

    # Create final output with all necessary data
    return [{
        "json": {
            "scrapedContents": collected_content,
            "researchTopic": research_topic,
            "urlToScrape": url_to_scrape
        }
    }]