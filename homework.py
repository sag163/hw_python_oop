import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, Record):
        self.records.append(Record)
        
    def get_week_stats(self):
        summ7 = 0
        timedelta = dt.datetime.now().date() - dt.timedelta(6)
        for j in self.records:
            if   timedelta <= j.date <= dt.datetime.now().date():
                summ7 = summ7 + int(j.amount)
        return summ7

    def get_today_stats(self):
        summ = 0
        for i in range(len(self.records)):
            if self.records[i].date == (dt.datetime.now()).date():
                summ += self.records[i].amount
        return(summ)

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
        count = 0
        for i in range(len(self.records)):
            if self.records[i].date == (dt.datetime.now()).date():
                count += self.records[i].amount
        ost = float(self.limit - count) 
        
        if currency == 'eur':
            remainder = ost / self.EURO_RATE
            currency2 = 'Euro'
        elif currency == 'usd':
            remainder = ost / self.USD_RATE
            currency2 = 'USD'
        else:
            remainder = ost
            currency2 = 'руб'

        if ost > 0:
            print(ost)
            return(f'На сегодня осталось {round(remainder, 2)} {currency2}')
        elif ost == 0:
            return('Денег нет, держись')
        else:
            return(f'Денег нет, держись: твой долг - {abs(round(remainder, 2))} {currency2}')
        
        
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        count = 0
        for i in range(len(self.records)):
            if self.records[i].date == (dt.datetime.now()).date():
                count += self.records[i].amount 
        ost = self.limit - count 
        if count < self.limit and count > 0:
            N = self.limit - count
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {N} кКал')
        else:
            return("Хватит есть!") 


