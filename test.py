#this is for testing, not need

import requests 

artist = "Coldplay"
song = "Adventure of a Lifetie"

api_url = f"https://api.lyrics.ovh/v1/{artist}/{song}"

response = requests.get(api_url)

data = response.json()

print(data)