from lib.greet import *

def test_greet():
    result = greet('Amina')
    assert result == "Hello, Amina!"