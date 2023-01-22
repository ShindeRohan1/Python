#print("Addtion using module")
import ModuleOfAddition

def main():
    print("Enter first number")
    no1 = 11
    print("Enter second number")
    no2 = 10

    sum = ModuleOfAddition.Addition(no1,no2)

    print("Addition is",sum)
    print("In Addition8 ",__name__)

if __name__ == "__main__":
    main()