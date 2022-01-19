import requests
from dotenv import load_dotenv
import os

# To run this program you will need to create your own .env file and use your own credentials
# pixela user documentation: https://docs.pixe.la/entry/post-user
load_dotenv()
user_token = os.getenv('PIXELA_TOKEN')
username = os.getenv('PIXELA_USERNAME')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": user_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
