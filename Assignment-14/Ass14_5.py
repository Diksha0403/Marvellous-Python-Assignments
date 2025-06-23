class BackAccount:
    def __init__(self,a,n,b):
        self.AccountNo = a
        self.name = n
        self.balance = b

    def deposite(self):
        deposite_amount = float(input("Enter Deposite Amount: "))
        self.balance += deposite_amount
        print("New Deposite Amount: ",self.balance,"\n")

    def withdrow(self):
        withdrow_amount = float(input("Enter withdrow amount: "))
        if withdrow_amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= withdrow_amount
            print("withdrow amount: ",withdrow_amount)
            print("New Balance: ", self.balance,"\n")

    def DisplayBalace(self):
        print("Account Number: ",self.AccountNo)
        print("Name: ",self.name)
        print("Total Balance: ",self.balance, "\n")

def main():
    obj = BackAccount(101,"Rahul",10000)

    obj.DisplayBalace()
    obj.deposite()
    obj.withdrow()


if __name__=="__main__":
    main()