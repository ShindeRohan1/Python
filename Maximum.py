import moduleMaximum
def main():
    print("Enter first number")
    number1 = input()
    print("Enter second number")
    number2 = input()
    
    Max = moduleMaximum.maximum(int(number1) , int(number2))
    print("Maximum number is ",Max)

if __name__ == "__main__":
    main()