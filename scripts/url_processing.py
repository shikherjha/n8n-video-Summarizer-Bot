"""
URL Processing Module

This script processes URLs extracted from web pages,
converting relative URLs to absolute URLs and preparing them
for subsequent HTTP requests.
"""
import re
from urllib.parse import urljoin

def process_urls(items):
    """
    Process extracted URLs and convert relative URLs to absolute URLs.
    
    Args:
        items: n8n items array containing extracted links and original URL
        
    Returns:
        List of items with processed URLs
    """
    # Get the original URL passed from the metadata
    input_url = items[0]["json"].get("OriginalUrl")
    
    # Fallback if for some reason originalUrl is missing
    if not input_url:
        raise ValueError("No originalUrl in incoming data")
    
    # Pull out the origin (scheme + "://" + host[:port])
    origin_match = re.match(r"^(https?://[^/]+)", input_url)
    if not origin_match:
        raise ValueError(f"Invalid URL: {input_url}")
    
    base_url = origin_match.group(1)
    
    # Extract the links from previous node (HTML Extract Links)
    links = items[0]["json"].get("extractedLinks", [])
    
    results = []
    for link in links:
        # Convert relative link to absolute
        if not re.match(r"^https?://", link, re.IGNORECASE):
            # Use urljoin for proper URL joining
            full_link = urljoin(base_url, link)
        else:
            full_link = link
            
        results.append({
            "json": {
                "links": full_link
            }
        })
    
    return results