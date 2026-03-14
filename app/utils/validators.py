import uuid

def validate_amount(amount):
    return isinstance(amount, int) and amount >= 1

def validate_currency(currency):
    return isinstance(currency, str) and len(currency) == 3

def validate_email(email):
    return isinstance(email, str) and "@" in email and "." in email

def generate_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:6]}"