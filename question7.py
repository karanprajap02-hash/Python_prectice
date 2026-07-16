def reverse(script):
  print(script[::-1])
reverse(script=input("Enter a string: "))

# second approch

script=input("Enter a string: ")
def revers(script):
    new_str="" 
    for s in script:
        new_str= s+ new_str
    print(new_str)
revers(script)
# Third approch
# print(revers(script))

# fourth approch
script=input("Enter a string: ")
re="".join(reversed(script))
print(re)