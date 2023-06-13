import pytest
from lib.password_checker import PasswordChecker

def test_if_password_len_less_8():
    password = PasswordChecker()
    result = password.check('123456789')
    assert result == True

def test_short_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as err:
        password.check('1234')
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."