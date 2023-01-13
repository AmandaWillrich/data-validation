from datetime import datetime


class DatesBr:
    def __init__(self):
        self.register_moment = datetime.today()

    def register_month(self):
        months = ['janeiro', 'fevereiro', 'março',
                  'abril', 'maio', 'junho', 'julho', 'agosto',
                  'setembro', 'outubro', 'novembro', 'dezembro']
        reg_month = self.register_moment.month - 1
        return reg_month[months]

    def __str__(self):
        return self.format_date()

    def week_day(self):
        week_days = ['segunda', 'terça', 'quarta',
                     'quinta', 'sexta', 'sabado', 'domingo']
        week_day = self.register_moment.weekday()
        return week_days[week_day]

    def format_date(self):
        formatted_date = self.register_moment.strftime('%d/%m/%Y %H:%M')
        return formatted_date
