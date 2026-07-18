num=int(input("Enter integr value:"))
def length(num):
    n=abs(num) # it is absolute value ,remove negative
    count=0
    while n>0:
        count+=1
        n//=10
    print(f"length of value:{count}")
length(num)
