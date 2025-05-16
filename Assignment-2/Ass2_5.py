def is_prime(number):
  
  if number > 1:
    for i in range(2,number):
      if (number % i) == 0:
        return False
    return True
  else:
    return False
  
def main():
    val = int(input("Enter a number to check: "))

    Value = is_prime(val)

    # Condition Checking
    if is_prime(val):
        print("It is a Prime number.")
    else:
        print("It is not a Prime number.")


if __name__ == "__main__":
  main()


  



