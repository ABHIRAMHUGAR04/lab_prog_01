from evenodd import evenorodd

def test_even():
    assert evenorodd(10) == "Even"

def test_odd():
    assert evenorodd(7) == "Odd"