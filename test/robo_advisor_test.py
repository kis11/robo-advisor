
from app.roboadvisor import to_usd

def test_to_usd():
    result = to_usd(3)
    assert result == "$3.00"