from api.user_api import get_user_by_email,update_user,delete_user
from conftest import  create_user

#test case-1get user details by email
def test_get_user_by_email(create_user):
    email = create_user["email"]

    #call the api
    response = get_user_by_email(email)

    #debug and print responses
    print(response.status_code)
    print(response.text)

    # Convert response to JSON
    response_data = response.json()

    # add assertions
    assert response.status_code == 200  # api http status code
    assert response_data["responseCode"] == 200  # actual business code

    assert "user" in response_data
    assert isinstance(response_data["user"], dict)

    user = response_data["user"]

    assert user["email"] == create_user["email"]
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)

# testt case-2 update user account
def test_update_user_account(create_user):
    # step-1 get email from fixture
    email= create_user["email"]
    password = create_user["password"]

    # Step 2: create ONLY update payload (not full duplication)
    update_user_payload = {
        "email" : email,
        "password" : password,
        "company" : "Test Automation Company",
        "city" : "Williamsburg"
    }

    # Step-3 call api
    response = update_user(update_user_payload)

    #print and debug
    print(response.status_code)
    print(response.text)

    # convert response to json
    response_data = response.json()

    #assertions
    assert response.status_code == 200  # api http status code
    assert response_data["responseCode"] == 200  # actual business code
    assert response_data["message"] == "User updated!"

# test case-3 get user details after update
def test_get_user_after_update(create_user):
    # get details from fixture
    email = create_user["email"]
    password = create_user["password"]

    #step-1 update user
    update_payload ={
        "email" : email,
        "password" : password,
        "company" : "Test Automation Company",
        "city" : "Williamsburg"
    }

    update_response = update_user(update_payload)

    # STEP 2: GET user AFTER update (ONLY email needed)
    response = get_user_by_email(email)

    print(response.status_code)
    print(response.text)

    response_data = response.json()

    # STEP 3: basic validations
    assert response.status_code == 200
    assert response_data["responseCode"] == 200

    assert "user" in response_data
    assert isinstance(response_data["user"], dict)

    user = response_data["user"]

    # STEP 4: verify updated values
    assert user["email"] == email
    assert user["company"] == "Test Automation Company"
    assert user["city"] == "Williamsburg"

#test case -4 Delete user account
def test_delete_account(create_user):
    email = create_user["email"]
    password = create_user["password"]

    delete_account_payload= {
        "email" : email,
        "password" : password
    }

    response = delete_user(delete_account_payload)

    print(response.status_code)
    print(response.text)


    response_data = response.json()

    assert response.status_code == 200
    assert response_data["responseCode"] == 200
    assert  response_data["message"] == "Account deleted!"

# STEP 2: verify deletion (VERY IMPORTANT REAL QA STEP)
    verify_response = get_user_by_email(email)
    verify_data = verify_response.json()

    assert verify_data["responseCode"] == 404

    # STEP 3: flexible assertion (real-world safe)
    assert (
            verify_data.get("responseCode") in [404, 200]
            or "user" not in verify_data
            or verify_data.get("message") == "Account not found with this email, try another email!"
    )

    print("VERIFY STATUS:", verify_response.status_code)
    print("VERIFY RESPONSE:", verify_response.text)


