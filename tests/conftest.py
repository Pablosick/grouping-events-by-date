import pytest

from generation.gen_events import EventsGeneration


correct_data = EventsGeneration("2022-01-01", "2022-08-08")


@pytest.fixture(scope="function")
def get_events():
    validate_data = correct_data.generation_json()
    return validate_data