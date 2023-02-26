import requests
import os
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload

"""
    The upload functionality is possible only with OAuth.
"""

def upload_http():

    api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"
    videoId = "YzZUIYRCE38"
    url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet&key={api_key}"

    with open("videos/test1.mov", "rb") as f:
        video = f.read()

    response = requests.post(url, data = video)
    print(response.status_code)
    print(response.text)

def upload():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().insert(
        part="snippet",
        body={},

        media_body=MediaFileUpload("videos/test1.mov")
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    upload()