from sys import *

def Addition(Number1 , Number2):
    Ans = Number1 + Number2
    return Ans
def main():
    print("Welcome to :",argv[0])

    iNum1 = int(argv[1])
    iNum2 = int(argv[2])

    Answer = Addition(iNum1 , iNum2)

    print("Addition is :",Answer)

if __name__ == "__main__":
    main()