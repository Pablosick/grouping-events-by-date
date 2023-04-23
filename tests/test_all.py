from src.schmas.event import Event
from src.verification.checkclass import Check
from src.verification.check_group_proccessing import CheckGroupGeneration


def test_getting_data(get_events):
    Check(get_events).check_validate(Event)


def test_output_data(res_get_events):
    CheckGroupGeneration(res_get_events).check_keys()