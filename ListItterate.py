
#Data : Heterogenous
#Ordered = yes
#Indexed = yes
#Mutable = yes
#Duplicate = yes

Data = [11,21,51,101]

for i in Data:
    print(i,end = " ")
print()

print("output using for with index")
for no in range(0,len(Data)):
    print(Data[no],end = " ")
print()

print("output using while with index")

i = 0
while(i < len(Data)):
    print(Data[i],end = " ")
    i+=1
print()
