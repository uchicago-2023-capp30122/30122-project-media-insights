import requests
import os
import re
import googleapiclient.discovery

def get_comments(url_lst):
    return_lst = []

    for url in url_lst:

        get_request(videoId="YzZUIYRCE38")

def get_request(videoId="YzZUIYRCE38"):
    api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response

def get_comments_api(videoId="YzZUIYRCE38"):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="replies",
        videoId = videoId
    )
    response = request.execute()

    return response

url_lst = ["https://www.youtube.com/watch?v=jcgCSbiKoaI",
           "https://www.youtube.com/watch?v=vAQTBrOxUMU",
           "https://www.youtube.com/watch?v=EkbDQAH71Yg"]
get_comments(url_lst)


# Possibly think about storing data in database
    # db file, or json file.

# References
# https://github.com/youtube/api-samples
# https://developers.google.com/youtube/v3/docs/commentThreads/list
