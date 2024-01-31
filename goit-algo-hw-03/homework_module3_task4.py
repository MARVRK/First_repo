import datetime as dt
from datetime import datetime as dtd

def get_upcoming_birthdays(users=None):
    currentday=dtd.today().date()
    birthdays=[]
    for workers in users:
        bdate=workers["birthday"]
        bdate=str(currentday.year)+bdate[4:]
        bdate=dtd.strptime(bdate, "%Y.%m.%d").date()
        week_day=bdate.isoweekday()
        days_between=(bdate-currentday).days
        if 0<days_between<7:
            if week_day>6:
                birthdays.append({'name':workers['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':workers['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (bdate+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':workers['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"} ]

print(get_upcoming_birthdays(users))

