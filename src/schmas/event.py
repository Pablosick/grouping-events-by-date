import datetime
import string

from pydantic import BaseModel, validator

from src.error.input_errors import DateErrors, TypesError, NamesError, MembersError, PlaceError
from src.enums.type_events_enum import EventType


class Event(BaseModel):
    date: str
    type: str
    name: str
    members: list
    place: str


    @validator("date")
    def validate_date(cls, date):
        correct_date = str(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) == date
        if correct_date:
            return date
        else:
            raise ValueError(DateErrors.WRONG_DATE.value)


    @validator("type")
    def validate_type(cls, types):
        if types in EventType[types].value:
            return types
        else:
            raise ValueError(TypesError.WRONG_TYPE.value)


    @validator("name")
    def validate_name(cls, name):
        special_characters = len([index for index in string.punctuation if index in name]) == 0
        if special_characters:
            return name
        else:
            raise ValueError(NamesError.WRONG_NAME.value)


    @validator("members")
    def validate_members(cls, members):
        elements_not_numbers = len(members) == len([i for i in members if type(i) != int])
        if elements_not_numbers:
            return members
        else:
            raise ValueError(MembersError.WRONG_MEMBERS.value)


    @validator("place")
    def validate_place(cls, place):
        not_number_string = len([i for i in place if i.isdigit()]) == 0
        if not_number_string:
            return place
        else:
            raise ValueError(PlaceError.WRONG_PLACE.value)


class ListEvents(BaseModel):
    events = Event