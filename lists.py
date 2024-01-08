my_list=[0,'Pyton',10,3,4,5,6,7,8,8,8,8,8,8]
c_ind= my_list.index('Pyton')               # looking for excatly index number of "something" inside the list
print(c_ind)
count_mylist=my_list.count(8)               #counting the "X" itmes in the list
#my_list.sort()                             #sorting the list of numbers (only)
#my_list.sort(reverse=True)                 #same, but in reverse sorting the list of numbers (only)
#my_;ist.sort(key-len)                      #sorting the list of numbers by lenght of symbols per index.
print(count_mylist)                         
print(len(my_list))                         #len calculate the itmes inside the list
print(my_list)