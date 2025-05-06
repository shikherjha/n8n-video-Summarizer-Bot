"""
D-ID Talk ID Processing

This script processes the response from the D-ID API,
extracting the talk ID and preserving other metadata.
"""

def process_talk_id(items):
    """
    Extract and process the talk ID from D-ID API response.
    
    Args:
        items: n8n items array containing D-ID API response
        
    Returns:
        List containing a single item with talk ID and metadata
    """
    response_data = items[0]["json"]
    
    # Safe check for ID in various places it might be
    talk_id = 'unknown'
    if response_data:
        if response_data.get("id"):
            talk_id = response_data["id"]
        elif response_data.get("result") and response_data["result"].get("id"):
            talk_id = response_data["result"]["id"]
    
    # Return data in expected format
    return [{
        "json": {
            "talkId": talk_id,
            "article": items[0]["json"].get("data", ""),
            "researchTopic": items[0]["json"].get("researchTopic", ""),
            # Include full response for debugging
            "fullResponse": response_data
        }
    }]