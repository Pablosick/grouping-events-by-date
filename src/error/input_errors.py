from enum import Enum


class DateErrors(Enum):
    WRONG_DATE = "Format does not meet requirements"


class TypesError(Enum):
    WRONG_TYPE = "Type does not match description"


class NamesError(Enum):
    WRONG_NAME = "The name does not match the conditions"


class MembersError(Enum):
    WRONG_MEMBERS = "Members cannot be a number"


class PlaceError(Enum):
    WRONG_PLACE = "The name of the meeting point cannot contain a number"