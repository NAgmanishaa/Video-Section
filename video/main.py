from googleapiclient.discovery import build

def get_video_subtitles(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get video captions
    
    captions_request = youtube.captions().list(
        part='snippet',
        videoId=video_id
    )
    captions_response = captions_request.execute()

    # Extract captions from the response
    subtitles = []
    for caption in captions_response['items']:
        caption_id = caption['id']
        caption_request = youtube.captions().download(
            id=caption_id,
            tfmt='srt'  # SubRip subtitle format
        )
        caption_content = caption_request.execute()
        subtitles.append(caption_content)

    return subtitles

if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'

    # Replace 'YOUR_VIDEO_ID' with the actual video ID you want subtitles for
    video_id = 'YOUR_VIDEO_ID'

    subtitles = get_video_subtitles(video_id, api_key)

    for i, subtitle in enumerate(subtitles, 1):
        print(f"Subtitle {i}:\n{subtitle}\n")
