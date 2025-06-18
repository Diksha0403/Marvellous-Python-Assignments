class BankAccount:
    ROI = 10.5
    def __init__(self,n,a):
        self.name = n
        self.amount = a
    
    def Display(self):
        print("Name: "+self.name)
        print("Amount: ",self.amount)

    def Deposit(self):
        deposit_amount = float(input("Enter deposit amount: "))
        self.amount += deposit_amount
        print("New Deposite Balance: ",self.amount)


    def Withdraw(self):
        
        withdraw_amount = float(input("Enter amount to withdraw for: "))
        if withdraw_amount > self.amount:
            print("Insufficient balance!")
        else:
            self.amount -= withdraw_amount
            print("Withdrawn Amount: ",withdraw_amount)
            print("New Balance: ",self.amount)

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print("Total Interest: ",interest)

def main():
    obj1 =BankAccount("Rahul",1000)

    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()

    print("---------------")

    obj2 =BankAccount("Ruhe",5000)

    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()



if __name__=="__main__":
    main()
