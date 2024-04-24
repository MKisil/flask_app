import re


def is_valid_phone_number(phone):
    pattern = re.compile(r"^\+?(\d{1,3})?[-. ]?(\(\d{1,3}\)|\d{1,3})?[-. ]?\d{1,4}[-. ]?\d{1,4}[-. ]?\d{1,4}$")

    if pattern.match(phone):
        return True
    else:
        return False


def is_valid_contact_name(name):
    if 1 <= len(name) <= 100:
        return True
    return False


def is_valid_contact_message(name):
    if 1 <= len(name) <= 10000:
        return True
    return False
