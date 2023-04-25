from src.schmas.event import Event
from src.verification.checkclass import InputValidation


def test_getting_data(get_events):
    """
    Entry compliance check
    :param get_events: fixture
    """
    status_received_data = InputValidation(get_events)
    status_received_data.check_validate(Event)
