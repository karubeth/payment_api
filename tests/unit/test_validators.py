from app.utils.validators import *

def test_validate_amount_valid():
    assert validate_amount(100)

def test_validate_amount_zero():
    assert not validate_amount(0)

def test_validate_amount_negative():
    assert not validate_amount(-1)

def test_validate_amount_decimal():
    assert not validate_amount(9.99)

def test_validate_currency_valid():
    assert validate_currency("usd")

def test_validate_currency_invalid():
    assert not validate_currency("us")

def test_validate_email_valid():
    assert validate_email("alice@example.com")

def test_validate_email_invalid():
    assert not validate_email("aliceexample.com")

def test_generate_id_prefix():
    assert generate_id("pay").startswith("pay_")