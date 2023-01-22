class Arithmatic:

    def __init__(self,A,B):
        print("Inside init meathoed")
        self.No1 = A
        self.No2 = B
    
    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans
    


def main():
    print("Inside main meathoed")

    obj = Arithmatic(11,12)

    Output = obj.Addition()
    print("Addition is ",Output)



if __name__ == "__main__":
    main()