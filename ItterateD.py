Batches = {"PPA" : 18000 , "LB" : 16000 , "Python" : 16500 ,"Angular" : 15000}

print("Data of Dictonary", Batches)

print("Data traversal using for loop")

for x in Batches:
    print(x)

for x in Batches:
    print(x,Batches[x])


for x in Batches:
    print(x,Batches.get(x))