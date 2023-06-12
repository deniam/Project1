from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(6)
    result = counter.report()
    assert result == "Counted to 6 so far."