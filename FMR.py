def CheckEven(No):
    return (No % 2 == 0)

def Double(No):
    return No * 2

def Sum(A,B):
    return A + B

def filterX(Helper_Function,Data):
    Result = []
    for No in  Data:
        if(Helper_Function(No) == True):
            Result.append(No)
    
    return Result

def main():
    print("Enter Number of elements you want to enter")
    iSize =  int(input())

    Data_input = []
    print("Plese enter the data")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_input.append(Value)
    
    print("Original data is ",Data_input)
    print("Type of original data is",type(Data_input))

    Data_Filter = filterX(CheckEven,Data_input)

    print("Data after filter is ",Data_Filter)


if __name__ == "__main__":
    main()