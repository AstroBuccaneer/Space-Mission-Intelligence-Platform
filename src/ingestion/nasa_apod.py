import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod"

params={"api_key": api_key}
response = requests.get(url, params=params)


print("Status Code:", response.status_code)
print("Response:", response.json())



