first=int(input("Enter first no: "))
second=int(input("Enter second no: "))
def gcd_or_hcf(num1,num2):
  while num2:
    num1,num2= num2,num1%num2
  return num1
result= gcd_or_hcf(first,second)
print(f"Reult hcf:{result}")
 
