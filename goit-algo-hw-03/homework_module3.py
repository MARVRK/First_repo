# ################################################ <---- TASK 1
from datetime import datetime

def get_days_from_today(date: str):
    try:
        date = datetime.fromisoformat(date)
        today_date= datetime.today()
        total= int((today_date-date).days)
        print(f"{total} days")
    except ValueError:
            print("Invalid ISOFormat , please use format YYYY-MM-DD")
    

  
provide_date="2024-01-23"   
to_summon_function=get_days_from_today(provide_date)
    
################################################### <----- Please check alternative solution for Task 1

# from datetime import datetime

# def get_days_from_today(date_is, format_is):
#     date=datetime.strptime(date_is, format_is)
#     today=datetime.today()
#     print(((date-today).days),"days")
    
# while True:
#         try:   
#             date_is=input("Write date with '.' spacing format: ")
#             format_is="%Y.%m.%d"
#             to_summon_function=get_days_from_today(date_is,format_is)
#         except ValueError :
#             print(f"date_is {date_is} does not match format YYYY.MM.DD")
#         break

# ################################################ <---- TASK 2