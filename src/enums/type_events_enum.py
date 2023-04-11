from enum import Enum


class EventType(Enum):
    private = 'private'
    meeting = 'meeting'
    corporate = 'corporate'
    other = 'other'