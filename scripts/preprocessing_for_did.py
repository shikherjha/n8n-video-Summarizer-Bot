"""
D-ID API Preprocessing

This script formats the summarized content for the D-ID API,
which will generate a talking avatar video.
"""

def preprocess_for_did(items):
    """
    Format summarized content for the D-ID API.
    
    Args:
        items: n8n items array containing LLM-generated summary
        
    Returns:
        List of items with properly formatted D-ID API request data
    """
    # Initialize the result array
    result = []

    for item in items:
        content_text = ""
        
        # Navigate the specific path to get the content
        try:
            # This assumes item has json field with choices
            content_text = item['json']['choices'][0]['message']['content']
        except (KeyError, IndexError, TypeError):
            # If direct path fails, try alternative paths
            try:
                if 'choices' in item:
                    content_text = item['choices'][0]['message']['content']
            except (KeyError, IndexError, TypeError):
                try:
                    if 'message' in item and 'content' in item['message']:
                        content_text = item['message']['content']
                except (KeyError, TypeError):
                    content_text = "Could not extract content"
        
        # Create the output structure for d-id
        result_item = {
            "json": {
                "processedData": {
                    "source_url": "https://i.postimg.cc/7YDkZ9mR/sample.png",
                    "script": {
                        "type": "text",
                        "input": content_text
                    }
                }
            }
        }
        
        # Add to results
        result.append(result_item)

    return result