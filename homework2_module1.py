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
#     sum += num    # here we use sum to add all numbers appeard in cycle while
#     num-=1         # here we use -1 to avoid infinity loop.
#     print(sum)

######################## - Search "r" in string and count sum.

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for ar in message:                    # remember the new variable "ar" we shoudld be counted in the cycle FOR and after  make calcuations 
    if ar == "r" : 
        result += 1
    print(result)                   