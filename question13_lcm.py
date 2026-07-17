first=int(input("Enter first no: "))
second=int(input("Enter second no: "))
def lcm(first,second):
    max_num=max(first,second)
    while True:
        if max_num%first==0 and max_num%second==0:
            return max_num
        max_num+=1

print(lcm(first,second))