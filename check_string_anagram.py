string1=input("Enter the numbers: ")
string2=input("Enter the numbers: ")

def check_anagram(string1,string2):
    str1=string1.lower()
    str2=string2.lower()
    if len(str1)!= len(str2):
        return "Lenths of strings not equal."
    elif sorted(str1)==sorted(str2):
        print("String is equal")
    else:
        print("Sring is not equal")
        
check_anagram(string1,string2)