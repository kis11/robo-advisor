
from app.roboadvisor import to_usd, check_if_buy, get_response
import os
import mock


def test_to_usd():
    result = to_usd(3)
    assert result == "$3.00"


def test_check_if_buy():
    result = check_if_buy(10,10.53)
    assert result == "Buy!"

def test_get_response():
    symbol = "MS"
    parsed_response = get_response(symbol)
    assert "Time Series (Daily)" in parsed_response.keys()
