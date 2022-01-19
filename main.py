import requests
from dotenv import load_dotenv
import os

# NOTE: To run this program you will need to create your own .env file and use your own credentials
# NOTE: pixela user documentation: https://docs.pixe.la/entry/post-user
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

# NOTE: Comment this in when creating a user!
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# Developer Note: If using or testing this app, you can change these configs as needed to suit your needs
graph_config = {
    "id": "graph1",
    "name": "Meditation Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": user_token
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

