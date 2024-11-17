import datetime as dt

def datetime_now():
    dt_now = dt.datetime.now()
    print('текущее дата+время', dt_now)

def two_dates_delta():
    now = dt.datetime.now()
    then = dt.datetime(2007, 1, 23)
    delta = now - then
    print('разница ',delta.days) #.seconds

def str_to_date():
    date_string = '10-17-2020'
    date_object = dt.datetime.strptime(date_string, '%m-%d-%Y')
    print(type(date_object))
    print(date_object)

datetime_now()

two_dates_delta()

str_to_date()