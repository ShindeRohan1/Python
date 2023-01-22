class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()

    def Accept(self):
        print("Enter how many elements you want")
        self.size = int(input())

        print("plese enter the elements")
        value = 0
        for i in range(0,self.size):
            value = int(input())
            self.Arr.append(value)     

    def Display(self):
        print("Elements from list are>>")
        for i in range(0,self.size):
            print(self.Arr[i])

    def Summation(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.Arr[i]
        
        return sum
         

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print(Output)
    




if __name__ == "__main__":
    main()