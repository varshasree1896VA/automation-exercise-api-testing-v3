# utils/data_generator.py

from faker import Faker

fake = Faker()


def generate_name():
    return fake.name()


def generate_email():
    return fake.email()


def generate_password():
    return fake.password()