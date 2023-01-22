

def Demo():
    print("Inside Hello")

def Fun():
    print("Inside Fun")

def Hello(FPTR):
    print("Inside demo")
    FPTR()

Hello(Demo)
Hello(Fun)

 