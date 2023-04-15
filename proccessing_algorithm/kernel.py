import datetime

from src.enums.type_events_enum import EventType


class EventsHandler:

    __result_json = {}


    def working_with_events(self, raw_list):
        """
        The function starts the algorithm for working with events
        :param raw_list: List
        :return: Dict
        """
        for item in range(len(raw_list)):
            if self.__validate_keys(raw_list[item]) == raw_list[item]:
                self.__result_json.setdefault(self.__date_keys(raw_list[item]), [])
                self.__result_json[self.__date_keys(raw_list[item])].append(raw_list[item])
                self.__result_json[self.__date_keys(raw_list[item])] = sorted(self.__result_json[self.__date_keys(raw_list[
                                                                                                                   item])], key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False)
        return self.__result_json


    def __validate_keys(self, event):
        validate_type = event['type'] in EventType[event['type']].value and event['type'] not in EventType.other.value

        check_str_name = ' '.join([i for i in event['name'].split() if len(i) < 20 and i.isalnum()])
        validate_name = len(event['name']) < 100 and event['name'] == check_str_name

        validate_members_place = len(event['members']) != 0 and len(event['place']) != 0

        if validate_type and validate_name and validate_members_place:
            return event


    def __date_keys(self, event):
        new_keys_json = datetime.datetime.strptime(event['date'], '%Y-%m-%d %H:%M:%S')
        return str(new_keys_json.date())

