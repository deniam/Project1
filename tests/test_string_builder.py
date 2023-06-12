from lib.string_builder import *

def test_string_builder_output():
    string = StringBuilder()
    string.add('Yellow')
    result = string.output()
    assert result == "Yellow"
    
    

def test_string_builder_size():
    string = StringBuilder()
    string.add('Yellow')
    result = string.size()
    assert result == 6

def test_string_builder_with_multiple_strings():
    string = StringBuilder()
    string.add("Yellow")
    string.add(' ')
    string.add("Rain")
    result = string.output()
    assert result == "Yellow Rain"

