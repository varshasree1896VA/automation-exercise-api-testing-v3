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

