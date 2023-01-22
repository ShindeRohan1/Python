from sys import *

def main():
   

    for i in range(0,4,1):
        print("At index :",i, argv[i])
    
    i = 0
    while(i < 4):
          print("At index :",i, argv[i])
          i = i + 1



if __name__ == "__main__":
    main()