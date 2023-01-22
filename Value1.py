class Value:
    def __init__(self,Data):
        self.No = Data

    def SumFactors(self):
        sum = 0
        for i in range(1,self.No):
            if(self.No % i == 0):
                sum = sum + i 
        return sum

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if(self.No == Ans):
            return True
        else:
            return False

def main():

    print("Enter number")
    
    A = int(input())

    obj = Value(A)
    Ret = obj.CheckPerfect()
    if(Ret == True):
        print("perfect")
    else:
        print("Not perfect")

if __name__ == "__main__":
    main()