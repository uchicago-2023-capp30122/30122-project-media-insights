import requests
import os
import googleapiclient.discovery

def get_comments():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="replies",
        videoId = "YzZUIYRCE38"
    )
    response = request.execute()

    for comment in response['items']:
        comment = comment.get('replies', None)
        if comment:
            print(comment['comments'][0]['snippet']['textOriginal'], "\n")

def get_comments_simple():

    api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"
    videoId = "YzZUIYRCE38"

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response

# response = {'kind': 'youtube#commentThreadListResponse', 'etag': 'DvEonU8ukojPWI9Q3jTtKZeXRM8', 'nextPageToken': 'QURTSl9pMFdpQk1rOFpfRG1XWkQ0MFNBYkIzZjByWF94d0ExZXhQTDRlSWpYd2JlRjRBZ0JibDVtMlMzNk5SUUswR1QxcjRBc3VlSXFaWQ==', 'pageInfo': {'totalResults': 20, 'resultsPerPage': 20}, 'items': [{'kind': 'youtube#commentThread', 'etag': '6KzJRCc2b67D_RaygjtOml88F4A', 'id': 'Ugwye5aOxwvHdAmzpzB4AaABAg', 'replies': {'comments': [{'kind': 'youtube#comment', 'etag': 'ndOW-I8UOm4sc1P5k-bi1TGJm2k', 'id': 'Ugwye5aOxwvHdAmzpzB4AaABAg.9j-U6vJMvEy9jFhxHAFkfu', 'snippet': {'videoId': 'YzZUIYRCE38', 'textDisplay': 'Row vectors are written as v^T. It&#39;s just a convention to distinguish them from column vectors.', 'textOriginal': "Row vectors are written as v^T. It's just a convention to distinguish them from column vectors.", 'parentId': 'Ugwye5aOxwvHdAmzpzB4AaABAg', 'authorDisplayName': 'APaleDot', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AL5GRJUIqDQziNWVqHA2ORbsDU9aRMIeTZbR0I2pRtI=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCulzFPTd4ygqJ7Yt3MhuBiA', 'authorChannelId': {'value': 'UCulzFPTd4ygqJ7Yt3MhuBiA'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 0, 'publishedAt': '2022-12-05T11:23:24Z', 'updatedAt': '2022-12-05T11:23:55Z'}}]}}, {'kind': 'youtube#commentThread', 'etag': 'gvPpOa7JDe-8_So8691NxVrFo5Q', 'id': 'UgyOOTmmOkcnHf4nJpl4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'gOCBU3aerXnBrqi2rBTlBgCsF2g', 'id': 'UgwZ_g3vhbi8MoR_QRB4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'tx732J75HfRyzs-Xt6RmoEZSgic', 'id': 'UgxCVHOu16BanT_XVhp4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'EcP67vOkHp6Yei_-wxLpeknpd4M', 'id': 'Ugy5lH3QrCFvuhBNusd4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'HcpxHKwg9cLuHomxnhplliV9NYI', 'id': 'UgytS8IBHg2N7tko4Sp4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'S9pSkpJrc8njdFqvnn8kFyUrQnI', 'id': 'UgxRRUuQaLYqMdABewl4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'UQ7JJUSvsGoGoHKay-rF6bFhnX0', 'id': 'UgwmgY4J2egRcXKJOLh4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': '13p_la7_IBFeEvC03phemevENvY', 'id': 'UgyUBuVCdeKwRexhaZB4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': '-pBH93UeMnIMKCoGEJS8f8QhJzM', 'id': 'UgxGsWGgsHdeFfO4n854AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'kUBFFLbo3L5xv76bmC7JbA8MkIs', 'id': 'UgzEyBcbzvOtvHQJZyF4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'AScI6hvZR78RDyxVFf8_0ZIWd1I', 'id': 'Ugx8Oi5SQpUdp8D3L7R4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'QCaQqdY1jdWafes_tuSpi_Ef1HQ', 'id': 'UgzH0KqxM3iC_0ONofp4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'NGrkgXKsNRPcun5VFjHgKCwunrY', 'id': 'UgxBNj4WcfNrxiWQJht4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': '-GUpog_nV7ynMD80SA249jENDIw', 'id': 'UgxsJHzRhlQPdwT2vER4AaABAg', 'replies': {'comments': [{'kind': 'youtube#comment', 'etag': 'PVw2WsXPm0kEpi1k_9hL08QVXCM', 'id': 'UgxsJHzRhlQPdwT2vER4AaABAg.9XoP30EOwZk9jFiJeLuMwq', 'snippet': {'videoId': 'YzZUIYRCE38', 'textDisplay': 'Matrix multiplication distributes over addition because it is linear. Dot product also distributes for the same reason, if you prefer to look at it that way.', 'textOriginal': 'Matrix multiplication distributes over addition because it is linear. Dot product also distributes for the same reason, if you prefer to look at it that way.', 'parentId': 'UgxsJHzRhlQPdwT2vER4AaABAg', 'authorDisplayName': 'APaleDot', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AL5GRJUIqDQziNWVqHA2ORbsDU9aRMIeTZbR0I2pRtI=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCulzFPTd4ygqJ7Yt3MhuBiA', 'authorChannelId': {'value': 'UCulzFPTd4ygqJ7Yt3MhuBiA'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 0, 'publishedAt': '2022-12-05T11:26:35Z', 'updatedAt': '2022-12-05T11:26:35Z'}}]}}, {'kind': 'youtube#commentThread', 'etag': 'gW0AERTAdkXVl_gU8OsNyDJkx_0', 'id': 'Ugyt06yx7KgdBcZPQn94AaABAg'}, {'kind': 'youtube#commentThread', 'etag': '8KVKrpe-1Xz93NLXfCVFXrzj_Xo', 'id': 'UgxgEFI5QddEkFem21t4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'VVIxM7hsAPAnBKRisIkd68qiMUc', 'id': 'UgwnWDIGNr1Yx7lI5el4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'pQ2aR0seAE0Rg-8rbKJyTcLwBfY', 'id': 'UgwBNpAyBjGvjOgWUah4AaABAg'}, {'kind': 'youtube#commentThread', 'etag': 'cKQKDx09-vKF-Sz6ARty2RzFR3s', 'id': 'UgwL3Tv-24W-5Xzus2x4AaABAg'}]}
response = get_comments_simple()
print(response)


# Possibly think about storing data in database
    # db file, or json file.



# References
# https://github.com/youtube/api-samples
# https://developers.google.com/youtube/v3/docs/commentThreads/list
