class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {self.rented_or_not()}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split(".")
        month = DVD.return_month(date[1])
        return cls(name, id, int(date[2]), month, age_restriction)

    @staticmethod
    def return_month(month_date):
        month = {'01': 'Janauary',
                 '02': 'February',
                 '03': 'March',
                 '04': 'April',
                 '05': 'May',
                 '06': 'June',
                 '07': 'July',
                 '08': 'August',
                 '09': 'September',
                 '10': 'October',
                 '11': 'November',
                 '12': 'December'}
        for k, v in month.items():
            if k == month_date:
                return v

    def rented_or_not(self):
        rented = "not rented"
        if self.is_rented:
            rented = "rented"
        return rented
