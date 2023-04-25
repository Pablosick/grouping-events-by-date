from src.verification.check_group_proccessing import CheckGroupGeneration
from src.schmas.event import Event


def test_output_data(res_get_events):
    """
    Checking the output against the specified requirements
    :param res_get_events: fixture
    """
    final_result = CheckGroupGeneration(res_get_events)
    final_result.check_keys()
    final_result.output_validation(Event)
