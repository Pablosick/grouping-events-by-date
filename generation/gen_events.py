import datetime
import random
import string

from faker import Faker

from src.enums.type_events_enum import EventType


class EventsGeneration:
    __fake = Faker()  # Экземпляр класса Faker
    __listEvents = []  # Список событий
    __oneEvent = dict.fromkeys(
        ["date", "type", "name", "members", "place"]
    )  # Генерация ключей одного события

    def __init__(self, start_date, final_date):
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.final_date = datetime.datetime.strptime(final_date, "%Y-%m-%d")

    def generation_json(self):
        """
        The function generates random events
        :return: Dict
        """
        result_dictionary = self.main_dictionary_generation()
        return result_dictionary

    def main_dictionary_generation(self):
        for rand_events in range(random.randint(100, 10000)):
            self.__listEvents.append(
                self.__adding_a_single_event(self.__oneEvent.copy())
            )
        output_dictionary = {"events": self.__listEvents}
        return output_dictionary

    def __adding_a_single_event(self, input_dict):
        for keys in input_dict:
            if keys == "date":
                self.__date_generation(input_dict)
            elif keys == "type":
                self.__type_generation(input_dict)
            elif keys == "name":
                self.__name_generation(input_dict)
            elif keys == "members":
                self.__members_generation(input_dict)
            elif keys == "place":
                self.__place_generation(input_dict)
        return input_dict

    def __date_generation(self, date_key):
        date_range = self.final_date - self.start_date
        seconds_range = (date_range.days * 24 * 60 * 60) + date_range.seconds
        date_key["date"] = str(
            self.start_date
            + datetime.timedelta(seconds=random.randrange(seconds_range))
        )
        return date_key

    def __type_generation(self, type_key):
        type_key["type"] = random.choice([i.value for i in EventType])
        return type_key

    def __name_generation(self, name_key):
        rand_name = "".join(
            random.choice(string.ascii_lowercase + string.digits + " ")
            for j in range(random.randint(0, 150))
        )
        name_key["name"] = rand_name
        return name_key

    def __members_generation(self, members_key):
        members_key["members"] = [
            self.__fake.first_name() for i in range(random.randint(0, 10))
        ]
        return members_key

    def __place_generation(self, place_key):
        rand_place = [
            "telegram",
            "zoom",
            "".join(
                random.choice(string.ascii_lowercase)
                for j in range(random.randint(0, 15))
            ),
        ]
        place_key["place"] = random.choice(rand_place)
        return place_key
