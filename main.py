import requests
from dotenv import load_dotenv
import os
from datetime import datetime

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
graphID = "graph1"
graph_config = {
    "id": graphID,
    "name": "Meditation Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": user_token
}

# NOTE: Comment in to create graph using graph_config
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

fill_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}"
now = datetime.now()
date = now.strftime("%Y%m%d")

pixel_config = {
    "date": date,
    "quantity": "10.0"
}

# NOTE: Comment this in when filling a pixel
# pixel_response = requests.post(url=fill_pixel_endpoint, json=pixel_config, headers=headers)

# NOTE: Edit any information necessary for the update
date_to_update = datetime(year=2022, month=1, day=17)
update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphID}/{date_to_update.strftime('%Y%m%d')}"

update_config = {
    "quantity": "15.5"
}

# NOTE: Comment this in to update a datapoint
# update_response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
