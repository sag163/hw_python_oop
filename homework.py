import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, Record):
        self.records.append(Record)
        
    def get_week_stats(self):
        week_consumption = 0
        timedelta = dt.datetime.now().date() - dt.timedelta(6)
        for record in self.records:
            if timedelta <= record.date <= dt.datetime.now().date():
                week_consumption = week_consumption + int(record.amount)
        return week_consumption

    def get_today_stats(self):
        today_consumption = 0
        for record in self.records:
            if record.date == (dt.datetime.now()).date():
                today_consumption += record.amount
        return(today_consumption)

class Record:
    def __init__(self, amount, comment, date = ""):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = (dt.datetime.now()).date()
        else:
            self.date = (dt.datetime.strptime(date, '%d.%m.%Y')).date()

class CashCalculator(Calculator):
    USD_RATE = 63.34
    EURO_RATE = 69.16 
    def get_today_cash_remained(self, currency):
        spent_today = 0
        
        for record in self.records:
            if record.date == (dt.datetime.now()).date():
                spent_today += record.amount
        daily_balance = float(self.limit - spent_today)   
        euro = abs(round(daily_balance/self.EURO_RATE, 2))   #Много различных вариантов перебирал, но решил использовать такую конструкцию перевода валюты, чтобы не загромождать словарь
        dollar = abs(round(daily_balance/ self.USD_RATE, 2))
        ruble = abs(round(daily_balance, 2))
        dict_money = {'eur':['Euro', euro], 'usd':['USD', dollar], 'rub':['руб', ruble]}
       
        if daily_balance > 0:
            return(f'На сегодня осталось {(dict_money[currency])[1]} {(dict_money[currency])[0]}')
        elif daily_balance == 0:
            return('Денег нет, держись')
        else:
            return f'Денег нет, держись: твой долг - {(dict_money[currency])[1]} {(dict_money[currency])[0]}'
        
        
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        spent_today = self.get_today_stats()
        if spent_today < self.limit and spent_today > 0:
            remains = self.limit - spent_today
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remains} кКал')
        else:
            return("Хватит есть!")


