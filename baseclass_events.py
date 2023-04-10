import json

import datetime

from src.enums.type_events_enum import EventType


class EventsHandler:

    result_json = {}

    def __init__(self, input_json, o_json):
        self.input_json = input_json
        self.o_json = o_json


    def get_result(self):
        raw_list_events = self.running_raw_json()
        return self.working_with_events(raw_list_events)


    def working_with_events(self, raw_list):
        for item in range(len(raw_list)):
            if self.validate_keys(raw_list[item]) == raw_list[item]:
                self.result_json.setdefault(self.date_keys(raw_list[item]), [])
                self.result_json[self.date_keys(raw_list[item])].append(raw_list[item])
                self.result_json[self.date_keys(raw_list[item])] = sorted(self.result_json[self.date_keys(raw_list[item])],
                                                                          key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S.%f'), reverse=False)
        return self.output_json(self.result_json)


    def validate_keys(self, event):
        validate_type = event['type'] in EventType[event['type']].value and event['type'] not in EventType.other.value

        check_str_name = ' '.join([i for i in event['name'].split() if len(i) < 20 and i.isalnum()])
        validate_name = len(event['name']) < 100 and event['name'] == check_str_name

        validate_members_place = len(event['members']) != 0 and len(event['place']) != 0

        if validate_type and validate_name and validate_members_place:
            return event


    def date_keys(self, event):
        new_keys_json = datetime.datetime.strptime(event['date'], '%Y-%m-%d %H:%M:%S.%f')
        return str(new_keys_json.date())


    def running_raw_json(self):
        with open(self.input_json, 'r', encoding='utf8') as raw_json:
            json_in_dict = json.load(raw_json)['events']
        return json_in_dict


    def output_json(self, json_structure):
        with open(self.o_json, 'w',  encoding='utf8') as output_json:
            result_dict_in_json = json.dump(json_structure, output_json)
        return result_dict_in_json