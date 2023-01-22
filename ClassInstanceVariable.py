
class Pet():  
    animal = "dog"                  #class variable

    def __init__(self,breed,prise):
        self.breed = breed
        self.prise = prise        #instance variable


def main():
    Moti = Pet("Gavthi","100000")

    print(Moti.animal)
    print(Moti.breed)


if __name__ == "__main__":
    main()