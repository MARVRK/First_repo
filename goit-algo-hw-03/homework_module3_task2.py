################################################
import random

def get_numbers_ticket(min, max, quantity):
        list=[]
        random_list=random.randint(min,max)

        if max < quantity:
             raise ValueError("The max range cannot be less then quantity of shuffle numbers!")
        else:
            for i in range(quantity):
                while random_list in list:
                    random_list=random.randint(min,max)
                list.append(random_list)
            list.sort()
        return list
                   
min_numbers=1
max_numbers=1000
tickets_quantity=8
shuffle_list=get_numbers_ticket(min_numbers,max_numbers,tickets_quantity)
print(shuffle_list)