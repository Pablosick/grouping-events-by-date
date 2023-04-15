from src.schmas.event import Event


class Check:

    def __init__(self, query):
        self.query = query
        self.query_events = query["events"]


    def check_validate(self, schema):
        if isinstance(self.query_events, list):
            for item in range(len(self.query)):
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.query_events)
            return self