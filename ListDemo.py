print("Demonstration of List")

#Data : Heterogenous
#Ordered = yes
#Indexed = yes
#Mutable = yes
#Duplicate = yes


data = [11,21,51,101,11,21]#duplicata
data1 = [11,3.14,True,"hello"] #Heterogenous


print("data at index 2 :",data1[2])
print("data is ordered :",data1)
print("data duplicate",data)

print("List is mutable")
data.append(201)
print("data after append",data)
data.pop()
print("data agter pop",data)