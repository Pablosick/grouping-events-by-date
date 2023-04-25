import datetime


class CheckGroupGeneration:
    def __init__(self, out_res):
        self.out_res = out_res

    def __correct_date(self, value_date):
        rec_date = datetime.datetime.strptime(value_date, "%Y-%m-%d %H:%M:%S")
        return str(rec_date.date())

    def check_keys(self):
        if isinstance(self.out_res, dict):
            for k, v in self.out_res.items():
                assert k == self.__correct_date(v[0]["date"])
        return self

    def output_validation(self, schema):
        for res_list in self.out_res.values():
            for items in res_list:
                schema.parse_obj(items)
        return self
