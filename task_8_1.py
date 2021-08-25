class DateTransform:
    def __init__(self, date_string):
        self.date_string = str(date_string)

    @classmethod
    def get_day_month_year(cls, date_string):
        date_list = date_string.split("-")

        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def valid_date(date_tuple):
        if 1 <= date_tuple[0] <= 31:
            if 1 <= date_tuple[1] <= 12:
                if 0 <= date_tuple[2] <= 2022:
                    return f"Такая дата действительно существует"
                else:
                    return f"Некорректный год"
            else:
                return f"Некорректный месяц"
        else:
            return f"Некорректный день"


current_date, not_exists_date = "24-08-2021", "25-99-1998"
print(DateTransform.get_day_month_year(current_date))
print(DateTransform.valid_date(DateTransform.get_day_month_year(not_exists_date)))
print(DateTransform.valid_date(DateTransform.get_day_month_year(current_date)))
