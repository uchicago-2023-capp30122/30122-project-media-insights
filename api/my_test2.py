# https://github.com/youtube/api-samples

import requests

api_key = "AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs"

url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q=surfing&key={api_key}"

response = requests.get(url)

print(response)