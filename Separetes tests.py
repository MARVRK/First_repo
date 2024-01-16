# # # print("hello word")
# # # print ('else')


# # numbers="DICK, 1, 3, 5, 8, 4, 5, 3 ,6 ,7 ,8 ,7, 2, 2 ,1"
# # odd_numbers = numbers[:5]
# # print(odd_numbers)


name = input("type your name qrwa :")
surname = input("and surname also: ")
age = input("and your oldfuck age please: ")
# ############################################## ----> how to make to make exceptacne in
try:
    age = int(age) 
    if str(age):
        print("Uh... is that in dog years?")  
except ValueError:
        print(f'{age}you should write the number...')   

##############################################
