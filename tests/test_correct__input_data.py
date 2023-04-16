from generation.gen_events import EventsGeneration

from src.schmas.event import Event
from src.verification.checkclass import Check

correct_data = EventsGeneration("2022-01-01", "2022-08-08")


def test_getting_data():
    validate_data = correct_data.generation_json()
    response = Check(validate_data)
    response.check_validate(Event)

