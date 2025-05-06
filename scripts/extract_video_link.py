"""
YouTube Video Link Extraction

This script extracts the YouTube video link from the YouTube upload response
and formats it for the final Telegram notification.
"""

def extract_video_link(items):
    """
    Extract YouTube video link from upload response.
    
    Args:
        items: n8n items array containing YouTube upload response
        
    Returns:
        List containing a single item with formatted video message
    """
    # Get the YouTube video ID from the previous node
    video_id = items[0]["json"].get("uploadId", "")  # Adjust property name if needed
    
    # Create a clean message with no special formatting issues
    message = {
        "text": f"Your research video has been completed and uploaded to YouTube!\n\nVideo URL: https://youtube.com/shorts/{video_id}",
        "videoUrl": f"https://youtube.com/shorts/{video_id}"
    }
    
    # Return the formatted data
    return [{"json": message}]