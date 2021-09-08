
# Import necessary libraries
import pandas as pd
import requests
import json


url = "https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4,sort_keys=True)
print(content)