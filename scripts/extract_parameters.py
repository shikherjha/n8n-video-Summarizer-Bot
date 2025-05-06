"""
Extract Research Topic and URL from Telegram Message

This script processes incoming Telegram messages to extract the research topic
and URL from messages formatted as "/research [topic]\n[url]".
"""
import re

def extract_parameters(items):
    """
    Extract research topic and URL from Telegram message.
    
    Format expected: "/research [Research Topic]\n[URL]"
    
    Args:
        items: n8n items array containing Telegram message data
        
    Returns:
        List of items with extracted research topic and URL
    """
    output = []
    
    for item in items:
        # Extract research topic and URL from the message
        message = item["json"]["message"]["text"]
        regex = r"^\/research\s+([^\n]+)\n(.+)$"
        match = re.match(regex, message)

        if match:
            research_topic = match.group(1).strip()
            url_to_scrape = match.group(2).strip()
            
            output.append({
                "json": {
                    "researchTopic": research_topic,
                    "urlToScrape": url_to_scrape,
                    "message": item["json"]["message"]
                }
            })
        else:
            output.append(item)

    return output