from sys import *
from ModuleOfAddition import Addition
def main():
    number1 = int(argv[1])
    number2 = int(argv[2])
    sum =  Addition(number1 , number2)
    print("Addition is ",sum)

if __name__ == "__main__":
    main()