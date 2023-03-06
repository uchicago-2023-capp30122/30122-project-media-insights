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

if __name__ == "__main__":
    upload_http()