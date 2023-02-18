def get_comments_simple():

    api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"
    videoId = "YzZUIYRCE38"

    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={videoId}&key={api_key}"
    response = requests.get(url).json()
    return response