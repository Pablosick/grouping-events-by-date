from baseclass_events import EventsHandler
from gen_events import EventsGeneration

#Test kernel program
start_json = EventsHandler('./mok_json/test.json', './mok_json/res.json')
start_json.get_result()

#Events generation
get_fired_events = EventsGeneration("2022-09-01", "2023-04-10")
get_fired_events.generation_json()