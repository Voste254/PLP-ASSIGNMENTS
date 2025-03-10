#creating empty list
my_list=[]
#appending the values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting 15
my_list.insert(1,15)
print(my_list)
#extending the list
list2=[50,60,70]
my_list.extend(list2)
print(my_list)
#removing last element
my_list.pop()
#sorting
my_list.sort()
print(my_list)
#find and print the value of 30
print(my_list.index(30))