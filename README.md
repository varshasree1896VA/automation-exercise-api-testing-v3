# Automation-exercise-api-project-v3

## API Automation Framework (Python + Pytest + Requests)

This project is an API automation testing framework built using Python, Pytest, and Requests for the Automation Exercise API.

---

## Tech Stack

- Python 3.8+
- Pytest
- Requests
- Faker
- Pytest Fixtures

---

## Project Structure
```
automation-exercise-api-project-v3/
│
├── api/
│   └── auth_api.py              # API layer (register, login methods)
│
├── tests/
│   └── test_auth.py             # Authentication test cases
│
├── utils/
│   └── data_generator.py       # Faker-based test data generator
│
├── conftest.py                 # Pytest fixtures (test setup)
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation

```
---

## What is Implemented

### Authentication Flow

- User Registration (POST create account)
- Valid Login
- Invalid Login
- Login with Null Values

---

## Key Concepts Used

- API Layer separation (auth_api)
- Fixture-based test setup (create_user)
- Faker data generation
- Positive and negative testing
- Reusable API methods

---

## Installation
```
pip install -r requirements.txt
```
## How to Run Tests
```
pytest -s -v
```
Run a specific file:
```
pytest -s tests/test_auth.py
```

### Current Status

- ✔ Authentication module completed
- ✔ Fixtures implemented
- ✔ Positive,negative test cases done
- ✔ Framework structure ready

### Next Steps

- Product API automation
- User API automation
- Data-driven testing 
- CI/CD integration with GitHub Actions
