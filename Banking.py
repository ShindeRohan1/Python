#Instance variable = Name , Amount, Address, AccountNo
#Instance Metod : CreateAccount(),DisplayAccountinfo()

#class Variable = Bank_Name, ROT_On_FD 
#clss method = DisplayBankInformation
#static method : display kyc
class BankAccount:
    Bank_Name = "HDFC bank PVT LTD"
    ROT_On_FD = 6.7


    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial amount:")
        self.Amount = int(input())

        print("Enter your Address :")
        self.Address = input()

        print("Enter your Account number :")
        self.AccountNo = int(input())

    def DisplayAccountinfo(self):
        print("Your account information is as below_________")
        print("Name of Account Holder",self.Name)
        print("Address of Account Holder",self.Address)
        print("Account Number of Account Holder",self.AccountNo)
        print("Current Amount in  Account",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of bank is :",cls.Bank_Name)
        print("Rate of intrest is ",cls.ROT_On_FD)

    @staticmethod
    def DesplayKycInfo():
        print("plese consider below KYC information")
        print("Accordinf to the rules of goverment of india you have to submit below documents")
        print("1 : clere and recent passport size photo")
        print("2 : photo of adharcard")
        print("3 : photo of pan card")

    def Deposite(self,value):
        self.Amount = self.Amount + value
    
    def Withdraw(self,value):
        self.Amount = self.Amount - value


        
def main():
    BankAccount.DesplayKycInfo()
    print("Name of bank",BankAccount.Bank_Name)
    print("Rate of intrest on fixed deposite",BankAccount.ROT_On_FD)

    BankAccount.DisplayBankInformation()

    obj1 = BankAccount()
    obj2 = BankAccount()
    
    print("creating first account")
    obj1.CreateAccount()
    print("creating second account")
    obj2.CreateAccount()

    obj1.DisplayAccountinfo()
    obj2.DisplayAccountinfo()

    obj1.Deposite(2000)
    obj2.Deposite(30)
    
    print("Amount of user 1 after deposite 2000",obj1.Amount)
    print("Amount of user 2 after deposite 30",obj2.Amount)

    obj1.Withdraw(2000)
    obj2.Withdraw(30)

    print("Amount of user 1 after withdrow 2000",obj1.Amount)
    print("Amount of user 2 after withdrow 30",obj2.Amount)







if __name__ == "__main__":
    main()