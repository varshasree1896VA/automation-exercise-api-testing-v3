import requests
from utils.config import BASE_URL

# Build function for get user details by email
def get_user_by_email(email):
    return requests.get(f"{BASE_URL}/getUserDetailByEmail?email={email}")

# Build function for update user details
def update_user(payload):
    return requests.post(f"{BASE_URL}/updateAccount", data=payload)

#build function for delete user
def delete_user(payload):
    return  requests.delete(f"{BASE_URL}/deleteAccount",data=payload)