# x=int(input(""))
# y=int(input(""))

# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")



############################################# my
# num = int(input("Enter a number: "))
# result = ""

# if num >  0:
#     if  num % 2 == 0:
#         result = print("Positive even number")
#     else:
#         result = print("Positive odd number")
# elif num < 0 :
#     result = print("Negative number")
# else:
#     result = print("It is zero")


# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)


# for i in range(2, 10, 2):
#     print(i)


# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)
    
# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
# #             break

####################################

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num >= 0:
#     sum += num    # here we use SUM to calcualte all numbers appeard in cycle WHILE
#     num-=1       # here we use -1 to avoid infinity loop during counitng sum for each iteration.
#     print(sum)

######################## - Search "r" in string and count sum.

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for ar in message:                    # remember the new variable "ar" we shoudld be counted in the cycle FOR and after  make calcuations 
#     if ar == "r" : 
#         result += 1
#         print(result)   
#####################################
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool / quantity
#     print(chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

###############################

# def invite_to_event(username: str)->str:
#     return(f'Dear {username}, we have the honour to invite you to our event')
# message = invite_to_event("Kielki")
# print(message)

# def format_string(string, length):
#     if len(string) >= len(length):
#         return string
    
    
# def values(x,y):
#     calculations=x+y
#     print(calculations)
#     x=3
#     y=1
#     calculations=x*y
#     print(calculations)
# values("a","b")

########################################### - how is roking integer
# def factorial(n:r)->str:
#     result = 1
#     for i in range(2, n + 2):
#         result *= i
#         print(result)
#     return result
# factorial(5)
########################
# def say(dick, big=1):
#     print(dick * big)

# say("this") 
# say('big', 5)

# #################################################
# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# keilki=string_to_codes("Dickenson")
# print(keilki)


###################################################
# def real_cost(base: int, discount: int = 0) -> int:
#         return int(base * (1 - discount))

# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)
# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')

#######################################################
# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result = arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))
#####################################################
# def first(size,*kielki):
#     file= size + len(kielki)
#     return file
# print(first(1,"frest","dupa"))
  
    
# def second(size,**kielki):
#     file= size + len(kielki)
#     return file
# print(second(1,comment_one="frest",comment_two=4))


# def first(size,*kielki):
#     file= size + len(kielki)
#     return file
#     print(file)
    
# # def second(size,**kielki):
# #     for key, value in kielki.items():
# #         print(f"{key}: {value}")
# #     return kielki
 
# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок
#     #          fibonacci(4) + fibonacci(3)
#     #          

# print(fibonacci(5)) # виведе 55


########################################
# s =""
# a = [1,4,7]
# b= [2,7]

# for n in a :
#     for m in b:
#         if (n+m)%2 ==0:
#             s+=str(a[(n+1)% len(a)])
#         else:
#             s+=str(b[(m+1)% len(b)])

 ###########################################################           

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)

#################################################################
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    this = factorial(n)/(factorial(n-k)*factorial(k))
    print(int(this))
    return int(this)

result=number_of_groups(50,7)
print(result)   
    
    