import requests    # Importing the requests from library
from utils.config import BASE_URL, REGISTER_ENDPOINT,LOGIN_ENDPOINT # import the endpoints and base-urls from config file

# build the register function
def register_user(payload):
    url = BASE_URL + REGISTER_ENDPOINT
    response = requests.post(url, data=payload)

    return response

#build login function
def login_user(payload):
    url = BASE_URL + LOGIN_ENDPOINT
    response = requests.post(url, data=payload)

    return response