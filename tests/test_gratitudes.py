from lib.gratitudes import *

def test_have_we_added_gratitude():
    gratitude = Gratitudes()
    gratitude.add('dog')
    result = gratitude.format()
    assert result == "Be grateful for: dog"

def test_have_we_added_few_gratitudes():
    gratitude = Gratitudes()
    gratitude.add('dog')
    gratitude.add('cat')
    gratitude.add('monkey')
    result = gratitude.format()
    assert result == "Be grateful for: dog, cat, monkey"

def test_empty_list_if_we_dont_added():
    gratitudes_list = Gratitudes()
    result = gratitudes_list.format()
    assert result == "Be grateful for: "