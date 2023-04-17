from src.schmas.event import Event
from src.verification.checkclass import Check


def test_getting_data(get_events):
    Check(get_events).check_validate(Event)

