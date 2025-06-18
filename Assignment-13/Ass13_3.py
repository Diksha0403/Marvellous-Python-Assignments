class Numbers:
    def __init__(self,value):
        self.value = value

    def ChkPrime(self):
        if self.value<=1:
            return False
    
        for i in range(2,self.value):
            if(self.value % i == 0):
                return False
        return True

    def ChkPerfect(self):
        sum_of_divisors = 0
        if self.value <= 0: 
            return False
    
        for i in range(1, self.value):  
            if self.value % i == 0:  
                sum_of_divisors += i  
        return True

    def SumFactors(self):
        sum_fact = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum_fact += i
        return sum_fact

    def Factors(self):
        print("Factors: ", end=" ")
        for i in range(1,self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

def main():
    obj1 = Numbers(28)
    obj2 = Numbers(17)

    print("Number: ",obj1.value)
    print("Is Prime?", obj1.ChkPrime())
    print("Is Perfect?", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())

    print("-------------------------------")
    
    print("Number: ",obj2.value)
    print("Is Prime?", obj2.ChkPrime())
    print("Is Perfect?", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())

if __name__=="__main__":
    main()
