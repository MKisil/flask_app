import re


def is_valid_email(email):
    if len(email) > 100:
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


def is_valid_password(password):
    if len(password) > 100:
        return False

    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+=\[\]{};:\'\\",.<>\/?~-]+$'
    if re.match(pattern, password):
        return True
    else:
        return False


def is_valid_name(name):
    if len(name) > 1000:
        return False

    return True
