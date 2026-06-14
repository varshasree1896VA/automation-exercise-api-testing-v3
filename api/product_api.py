import  requests
from utils.config import BASE_URL

# Build the get products function
def get_all_products():
    url = BASE_URL
    response = requests.get(f"{url}/productsList")
    return response

#build the function for product search
def search_product(payload):
    url = BASE_URL
    response = requests.post(f"{url}/searchProduct",data=payload)
    return  response
