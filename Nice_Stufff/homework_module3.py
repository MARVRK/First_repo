# ################################################
from datetime import datetime

def get_days_from_today(date_is, format_is):
    date=datetime.strptime(date_is, format_is)
    today=datetime.today()
    print(((date-today).days),"days")
    
while True:
        try:   
            date_is=input("Write date with '.' spacing format: ")
            format_is="%Y.%m.%d"
            call=get_days_from_today(date_is,format_is)
        except ValueError :
            print(f"date_is {date_is} does not match format YYYY.MM.DD")
        break