
################################################
import random

def get_numbers_ticket(min, max, quantity):
        set_tickets=set()
        list_tickets=list(set_tickets)

        try:
             if (min >=1 and max <=1000) and (quantity not in range(min,max)):
                return []
        except ValueError:
             return []
        
        for i in range(quantity):
             set_tickets.add(random.randint(min,max))
             list_tickets=list(sorted(set_tickets))
        return list_tickets
                   
min_numbers=1
max_numbers=1000
tickets_quantity=int(input("Choose number of tickets in range 1-1000: "))
shuffle_list=get_numbers_ticket(min_numbers,max_numbers,tickets_quantity)
print(shuffle_list)


################################################ <------------ alternative to task 2
# import random

# def get_numbers_ticket(min, max, quantity):
#         list_tickets=[]
#         try:
#              if (min >=1 and max <=1000) or (quantity in range(min,max)):
#                 random_list=random.randint(min,max)
#         except ValueError:
#             return []
        
#         for i in range(quantity):
#                 while random_list in list_tickets:
#                      random_list=random.randint(min,max)
#                 list_tickets.append(random_list)
#                 list_tickets.sort()              
#         return list_tickets
                    
# min_numbers=1
# max_numbers=1000
# tickets_quantity=int(input("Choose number of tickets in range 1-1000: "))
# shuffle_list=get_numbers_ticket(min_numbers,max_numbers,tickets_quantity)
# print(shuffle_list)