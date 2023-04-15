import argparse
import json


from generation.gen_events import EventsGeneration
from proccessing_algorithm.kernel import EventsHandler


parser = argparse.ArgumentParser()

input_argument = parser.add_argument("input_json", help="Enter the name of the input json file")
output_argument = parser.add_argument("output_json", help="Enter the name of the output json file")

console_entry = parser.parse_args()


class RunInConsole:

    get_fired_events = EventsGeneration("2022-09-01", "2023-04-10")  # Объект сгенерированного JSON файла
    get_grouped_events = EventsHandler()


    def assembled_program(self, first_argument, second_argument):
        received_dictionary = self.input_file(first_argument)
        return self.output_file(second_argument, received_dictionary)


    def input_file(self, entry):
        with open(f'./input_json/{entry}', 'w', encoding="utf8") as input_file:
            json.dump(self.get_fired_events.generation_json(), input_file, indent=4)

        with open(f'./input_json/{entry}', 'r', encoding='utf8') as raw_json:
            json_in_dict = json.load(raw_json)['events']
            return json_in_dict


    def output_file(self, o_positional, transformation):
        with open(f'./output_json/{o_positional}', 'w', encoding='utf8') as output_file:
            json.dump(self.get_grouped_events.working_with_events(transformation), output_file, indent=4)


user_launch = RunInConsole()
user_launch.assembled_program(console_entry.input_json, console_entry.output_json)
