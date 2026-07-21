num=int(input("Enter a number: "))
def binary(num):
    binary_num=""
    while num>0:
        n = num%2
        binary_num= str(n) + binary_num
        num//=2
    print(binary_num)
         

binary(num)