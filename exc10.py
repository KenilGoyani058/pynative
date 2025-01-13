#Merge two lists using the following condition --- odd numbers from the first list and even numbers from the second list.
list1=input("Enter numbers by space : ").split()
list2=input("Enter numbers by space : ").split()

list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]
list3=[]

for item in list1:
    if item % 2 != 0:
        list3.append(item)

for item in list2:
    if item % 2 == 0:
        list3.append(item)

print(list3)