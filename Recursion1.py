import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(10)
print(sys.getrecursionlimit())

def Display(No):
    iCnt = 0
    if(iCnt < No):
        print("Hello")
        iCnt = iCnt + 1
        Display(No)

Display(4)