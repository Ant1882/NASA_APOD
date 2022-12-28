import requests
import streamlit as st

api_key = "8xgcHJG1N3yBBngnzUqZfbsc8cSPY3kBY97yEq1v"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract image title, url, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

print(title)
print(image_url)
print(explanation)