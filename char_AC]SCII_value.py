char = [x for x in input("Enter the character: ").split(",")]
for c in char:
    print(f"The {c} vlaue : {ord(c)}")