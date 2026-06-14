from api.product_api import get_all_products, search_product

# TEST CASE 1: get all products (POSITIVE FLOW)
def test_get_all_products():

#call and get api response
    response = get_all_products()

#add debug prints or results
    print(response.status_code)
    print(response.text)

# Convert JSON response to Python dictionary

    response_data = response.json()


# add assertions
    assert response.status_code == 200  # api http status code
    assert response_data["responseCode"] == 200  # actual business code

    assert "products" in response_data
    assert isinstance(response_data["products"], list)
    assert len(response_data["products"]) > 0

    product_names = [p["name"] for p in response_data["products"]]
    assert "Blue Top" in product_names


#Test case-2 Search product
def test_search_product():
    search_product_payload = {
        "search_product": "Blue Top"
    }

    # call api response
    response = search_product(search_product_payload)

    #add debug prints or results
    print(response.status_code)
    print(response.text)

    # covert json response to python dictionary
    response_data = response.json()

# add assertions
    assert response.status_code == 200  # api http status code
    assert response_data["responseCode"] == 200  # actual business code

    products = response_data["products"]

    assert len(products) > 0

    for p in products:
        assert "Blue Top" in p["name"] or "top" in p["name"].lower()


# Test Cae-3 Search product by missing parameter (negative flow)
def test_search_product_missing_parameter():
    payload = {}

# call the api
    response = search_product( payload)

    # add debug prints or results
    print(response.status_code)
    print(response.text)

    # covert json response to python dictionary
    response_data = response.json()

    # add assertions
    assert response.status_code == 200
    assert response_data["responseCode"] == 400
    assert response_data["message"] == "Bad request, search_product parameter is missing in POST request."



