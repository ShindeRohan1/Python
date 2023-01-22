def main():
    
    try:
        print("Enter first number")
        No1 = int (input())

        print("Enter second number")
        No2 = int(input())
    
   
        Ans = No1 / No2
        print("Division is ",Ans)
    
    except ZeroDivisionError:
        print("Inside zerodivision")

    
    except ValueError:
        print("Inside value error")
    
    except Execution:                                          #msd
        print("Invalid last except block")

    finally:
        print("Inside finally blocc")



if __name__ == "__main__":
    main()