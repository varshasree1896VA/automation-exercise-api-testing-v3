# =========================================================
# IMPORTS (API LAYER)
# =========================================================
from api.auth_api import login_user, register_user

# =========================================================
# IMPORTS (FIXTURES)
# =========================================================
from conftest import create_user

# =========================================================
# IMPORTS (UTILS - USED FOR NEGATIVE TESTS)
# =========================================================
from utils.data_generator import generate_name, generate_email, generate_password


# =========================================================
# TEST CASE 1: REGISTER USER (POSITIVE FLOW)

def test_register_user(create_user):
    """
       Validate successful user registration using fixture-generated data.
       """

    # Get API response from fixture (user already created)
    response = create_user["response"]

#add debug prints or results
    print(response.status_code)
    print(response.text)

# Convert JSON response to Python dictionary

    response_data = response.json()

    # Add assertions
    assert response.status_code==200   # api https response code
    assert response_data["responseCode"] == 201 # actual business response code
    assert response_data["message"] == "User created!" # actual business message


#  create valid login test case -2
def test_login_user(create_user):
    """
      Validate login using credentials from the registered fixture user.
      """

    # Extract credentials from fixture (already registered user)
    email = create_user["email"]
    password = create_user["password"]

    # Prepare login request payload
    login_payload = {
        "email": email,
        "password": password
    }

    # send the login api like using reusable login api to get login response
    # Call login API
    response = login_user(login_payload)

    # add debug prints
    print(response.status_code)
    print(response.text)

    # Convert response to JSON
    response_data = response.json()

    # add assertions
    assert response.status_code==200   #api http status code
    assert response_data["responseCode"] == 200 # actual business code
    assert response_data["message"] == "User exists!"  # actual business message

# test case -3 Invalid login
def test_invalid_login():

    # generate email and password
    email = generate_email()
    password = generate_password()

    #register user for invalid login
    register_payload = {
        "name" : generate_name(),
        "email" : email,
        "password" : password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1995",
        "firstname": "John",
        "lastname": "Doe",
        "company": "ABC Company",
        "address1": "Street 1",
        "address2": "Apartment 100",
        "country": "USA",
        "zipcode": "30001",
        "state": "KY",
        "city": "Murphy",
        "mobile_number": "1111110001"

    }

    # call invalid register response
    response_register = register_user(register_payload)

    # now use this register response in invalid login
    login_invalid_payload = {
        "email" : email,
        "password" : "wrongPassword321"
    }

    print("invalid login payload:",login_invalid_payload)



    # now use login api
    response = login_user(login_invalid_payload)


    #print the response
    print(response.status_code)
    print(response.text)

    #Assertions
    response_data = response.json()
    assert response.status_code== 200
    assert response_data["responseCode"] == 404
    assert  response_data["message"] == "User not found!"

#Test case - 4 login with null values

def test_login_with_null_values():

    # create null payload
    login_null_payload = {
        "email" : None,
        "password" : None
    }

    #print null login to debug payload
    print("Null login:", login_null_payload)

    # call the login api
    response = login_user(login_null_payload)

    #print the responses
    print(response.status_code)
    print(response.text)

    #assertions
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["responseCode"] == 400
    assert response_data["message"] == "Bad request, email or password parameter is missing in POST request."




