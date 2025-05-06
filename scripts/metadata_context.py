"""
Metadata and Context Management

This script combines the generated summary with workflow metadata,
ensuring that context is preserved throughout the workflow.
"""

def process_metadata_and_context(item, first_item):
    """
    Process and combine metadata with generated content.
    
    Args:
        item: Current item being processed
        first_item: First item in the array (containing original metadata)
        
    Returns:
        Dictionary with combined metadata and content
    """
    article_text = item["json"].get("text", "")
    research_topic = (
        item["json"].get("researchTopic")
        or first_item["json"].get("researchTopic")
        or "Research Topic"
    )
    url_to_scrape = (
        item["json"].get("urlToScrape")
        or first_item["json"].get("OriginalUrl")
        or "URL"
    )
    return {
        "json": {
            "choices": [
                {
                    "message": {
                        "content": article_text
                    }
                }
            ],
            "researchTopic": research_topic,
            "urlToScrape": url_to_scrape
        }
    }

def process_items(items):
    """
    Process all items to ensure metadata context is preserved.
    
    Args:
        items: n8n items array
        
    Returns:
        List of items with preserved metadata context
    """
    first_item = items[0] if items else {}
    processed_items = [process_metadata_and_context(item, first_item) for item in items]
    
    return processed_items