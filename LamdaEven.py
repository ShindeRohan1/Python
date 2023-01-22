def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

Even = lambda No : No % 2 == 0

ret = Even(12)

if(ret == True):
    print("Even")
else:
    print("Odd")