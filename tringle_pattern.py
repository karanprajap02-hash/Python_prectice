num=int(input("Enter the size of tringle: "))
def tringle(num):
    for i in range(1,num+1):
        tri=[]
        for j in range(1,i+1):
          tri.append("*")
        print(tri)
tringle(num)

print("\n")
# other method
for i in range(1,num+1):
  print("*"*i)

print("\n")
# pyramid
for i in range(1,num+1):
  print(" "*(num-i)+"*"*(2*i-1))


