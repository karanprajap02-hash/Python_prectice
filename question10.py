num= int(input("Enter the number to check prime: "))
prime=True
for x in range(2,num):
    if num==2:
      prime=True
      break
    elif num<2:
      prime=False
      break
    elif num%x!=0:
        prime= False
print("It is not prime"if not prime else "It is prime")
    