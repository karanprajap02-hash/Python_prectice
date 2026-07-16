def str_len(str1): 
  count=0 
  for s in str1: 
    if s in ('a','e','i','o','u'): 
      count+=1
  print(count) 
str_len(str1=input("Enter the string: ").lower())

# second approch

str1=input("Enter the string: ").lower()
vowel=['a','e','o','i','u']
print(sum(1 for s in str1 if s in vowel))
