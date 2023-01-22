def Outer():
    print("Inside outer")

    def Inner():
        print("Inside Inner")
    print(id(Inner()))
    print(id(Inner))
    return Inner

ret = Outer()

print(id(ret))

ret()
