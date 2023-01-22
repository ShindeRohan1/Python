#function which accept nothing and return nothing
def Demo1():
    print("Inside Demo 1")

#function accept one parameter and return nothing
def Demo2(No):
    print("Inside Demo 2",No)

#function accepts one parameter and return one parameter 
def Demo3(No):
    print("inside Demo 3 with argument ",No)
    return No+2

#function accept two arguments and return one parameter
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add

#function accept two parameter and return two parameter
def Demo5(no1,no2):
    print("Inside Demo 5")
    Add = no1 + no2
    Sub =  no1 - no2
    return Add,Sub

def main():
    Demo1()

    Demo2("hallo")

    Ans = Demo3(10)
    print("return value of demo 3 is",Ans)

    Ans =  Demo4(10 , 11)
    print("Return value is :",Ans)
    
    Ans1,Ans2 = Demo5(11,10)
    print("First return value",Ans1)
    print("secont return value",Ans2)


if(__name__ == "__main__"):
    main()