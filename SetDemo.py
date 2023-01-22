print("Demonstration of Set")

#Data : Heterogenous
#Ordered = No
#Indexed = No
#Mutable = yes
#Duplicate = No


data = {11,21,51,101,11,21}#duplicata
data1 = {11,3.14,True,"hello"} #Heterogenous

print("data",data)
print("data is Heterogenous :",data1)
#print("data at index 2 :",data1[2])
print("data is unordered :",data1)


print("set is mutable")
data.add(201)
print("data after add",data)
data.remove(201)
print("data after remove",data)
