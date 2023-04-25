import pytest

from generation.gen_events import EventsGeneration
from proccessing_algorithm.kernel import EventsHandler


correct_data = EventsGeneration("2022-01-01", "2022-08-08")
group_data = EventsHandler()


@pytest.fixture(scope="function")
def get_events():
    validate_data = correct_data.generation_json()
    return validate_data


@pytest.fixture(scope="function")
def res_get_events():
    output_data = group_data.working_with_events(
        correct_data.generation_json()["events"]
    )
    return output_data
