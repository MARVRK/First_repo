# # # print("hello word")
# # # print ('else')


# # numbers="DICK, 1, 3, 5, 8, 4, 5, 3 ,6 ,7 ,8 ,7, 2, 2 ,1"
# # odd_numbers = numbers[:5]
# # print(odd_numbers)

# ############################################## --
# name = input("type your name qrwa :")
# surname = input("and surname also: ")
# age = input("and your oldfuck age please: ")

# try:
#     age = int(age) 
#     if str(age):
#         print("Uh... is that in dog years?")  
# except ValueError:
#         print(f'{age}you should write the number...')   

############################################## 

# text = "Zhis is Dome Strange Shit"
# alfabet = "aljdlsdmgnlsfdfgmnslkfg;msdlgmdslg"
# result = []
# for idnx, zis in enumerate(text):                      ---------> how to numerate symbols
#     #  if zis.lower() in alfabet:                      ---------> how to find similar sybmols in lists
#         print(idnx,zis)


# def code_translator(this_name: str)->dict :
#     codes={}
#     for zis in this_name:
#         if zis not in codes:
#             codes[zis]=ord(zis)
#     return codes
# call=code_translator("Zis shit is not good for you")
# print(call)


# def factorial(n):
#     if n < 2:
#         return n
#     else:
#         result = n * factorial(n-1)
#         return result
    
# call=factorial(4)

# def group_of_dicks(dick,pick):
#     result= factorial(dick)/(factorial(dick-pick)*factorial(pick))
#     return int(result)
# call = group_of_dicks(90,3)
# print(call)

# # if __name__ == '__main__':
# n = int(input())
# if n >=1 and n <=20:
#     total= n**2
#     print (total)
###################################
# def sos(el, list=[]):  #########################
#     list.append(el)
#     print(list)

# sos(1)
# sos(2)
# sos(3)

# #############################################
# new_list=[1,3,4,6,7,8,8,9,9]
# new_list=list(map(lambda x:x*2,new_list)) # -> you can filtre, double or divide in list items
# print(new_list)

##################################################
# new_list=[1,3,4,6,7,8,8,9,9]        # -> same as above
# filtered=[]
# for new_list in new_list:
#     if new_list%2==0:
#          filtered.append(new_list)
# print(filtered)
