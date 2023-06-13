import pytest # <-- New code
from lib.reminder_error import Reminder


def test_reminder_when_no_task_is_set():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"