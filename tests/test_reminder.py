from lib.reminder import *

def test_reminder():
    reminder = Reminder("Amina")
    reminder.remind_me_to("Bring washing in from outside")
    result = reminder.remind()
    assert result == "Bring washing in from outside, Amina!"