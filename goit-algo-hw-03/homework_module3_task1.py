
from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.fromisoformat(date)
        today_date= datetime.today()
        total= int((today_date-date).days)
        return total
    
    except ValueError:
            print("Invalid ISOFormat , please use format YYYY-MM-DD")
     
provide_date="2024-01-23"   
to_summon_function=get_days_from_today(provide_date)
print(f"{to_summon_function} days")
    
################################################### <----- Please check alternative solution (without return) for Task 1

# from datetime import datetime

# # def get_days_from_today(date_is, format_is):
# #     date=datetime.strptime(date_is, format_is)
# #     today_date= datetime.today()
# #     total= int((today_date-date).days)
# #     print(f"{total} days")
    
# # while True:
# #         try:   
# #             date_is=input("Write date based on format '%Y-%m-%d':  ")
# #             format_is="%Y-%m-%d"
# #             to_summon_function=get_days_from_today(date_is,format_is)
# #         except ValueError :
# #             print(f"date_is {date_is} does not match ISOformat YYYY-MM-DD")
# #         break

