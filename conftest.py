# a reusable setup function that runs before your test
#"pre-built test helper"
#WHY FIXTURES ARE USED IN REAL COMPANIES

#They help to:

#✔ remove duplicate code
#✔ centralize test setup
#✔ make tests cleaner
#✔ improve maintainability
#✔ support large test suites

#Simple analogy
#Without fixture:every test builds its own car
#With fixture:factory builds car once → tests just drive it

# CREATE REGISTRATION FIXTURE

#We will move your/Mine repeated register logic into a fixture.
#Add all imports

import  pytest
from utils.data_generator import generate_name,generate_email, generate_password
from api.auth_api import register_user

@pytest.fixture
def create_user():
    email = generate_email()
    password = generate_password()

    payload = {
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

    response = register_user(payload)

#return both value and response
    return  {
        "email" : email,
        "password" : password,
        "response": response
    }





