print("Fibonacci Series")
num=int(input("Enter the no:"))
def fibo(num):
    series=[]
    a,b=0,1
    for x in range(1,num+1):
        series.append(a)
        a,b=b,a+b
    print(f"series:{series}")
fibo(num)