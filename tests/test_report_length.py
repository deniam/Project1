from lib.report_length import *

def test_report_length():
    result = report_length('string')
    assert result == f"This string was 6 chararacters long"