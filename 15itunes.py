import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://www.youtube.com/results?search_query=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["videoName"])