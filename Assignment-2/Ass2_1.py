#import Arithematic
from Arithmatic import add,sub,mul,div

no1 =int(input("Enter first No: "))

no2 = int(input("Enter sencond No: "))


ans = add(no1, no2)
print("The Addition is: ",ans)

ans = sub(no1, no2)

print("The Subtraction is: ",ans)

ans = mul(no1, no2)
print("The Multiplication is: ",ans)

ans = div(no1, no2)

print("The Division is: ",ans)