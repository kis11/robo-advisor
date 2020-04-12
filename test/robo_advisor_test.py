
from app.roboadvisor import to_usd, check_if_buy
import os

def test_to_usd():
    result = to_usd(3)
    assert result == "$3.00"


def test_check_if_buy():
    result = check_if_buy(10,10.53)
    assert result == "Buy!"
