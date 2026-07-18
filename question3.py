lists=[]
print("Enter three no for find the largest:-")
for i in range(0,3):
    num=int(input("Enter the no: "))
    lists.append(num)
print(max(lists))

# numbers = list(map(int, input("Enter as many numbers as you want: ").split()))
# numbers = [int(x) for x in input("Enter student scores separated by spaces: ").split(",")]
