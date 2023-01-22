import os
import multiprocessing

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []

    pl = multiprocessing.Pool()
    Result = pl.map(Square , Data)

    print("Result after square oparation",Result)


if __name__ == "__main__":
    main()