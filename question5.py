a=int(input("Enter the number for factorial: "))
f=1
for x in range(1,a+1):
    f*=x
print(f"\nfactorial: {f}")