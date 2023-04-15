from pydantic import BaseModel, validator


class Event(BaseModel):
    date = str
    type = str
    name = str
    members = list
    place = str


class ListEvents(BaseModel):
    events = Event