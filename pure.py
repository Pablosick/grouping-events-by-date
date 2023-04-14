import argparse
import json


from gen_events import EventsGeneration
from kernel import EventsHandler


parser = argparse.ArgumentParser()


get_fired_events = EventsGeneration("2022-09-01", "2023-04-10")  # Объект сгенерированного JSON файла
get_grouped_events = EventsHandler()

#Позиционные аргументы
parser.add_argument("input_json", help="Enter the name of the input json file")
parser.add_argument("output_json", help="Enter the name of the output json file")





def input_argument(input_string, output_string):
    with open(input_string, 'w', encoding="utf8") as input_file:
        json.dump(get_fired_events.generation_json(), input_file, indent=4)


    with open(input_string, 'r', encoding='utf8') as raw_json:
        json_in_dict = json.load(raw_json)['events']
        test(output_string, json_in_dict)


def test(a, b):
    with open(a, 'w', encoding='utf8') as output_file:
        json.dump(get_grouped_events.working_with_events(b), output_file, indent=4)




# def output_json(output_string):
#     with open(output_string 'w',  encoding='utf8') as output_file:
#         json.dump(, output_file, indent=4)



console_entry = parser.parse_args()

input_argument(console_entry.input_json, console_entry.output_json)





