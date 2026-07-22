# simpel approch
data= {int(x) if x.isdigit() else x for x in (input("Enter the data (Seperate by ','):")).split(",")}
print(list(data))

# Also use this proch for better execution (without need of comma(,))
# # This regular expression extracts all numbers and operator symbols automatically
# expression = re.findall(r'\d+|[+\-*/]\\w', input("Enter expression: "))

import re
expression = re.findall(r'\w', input("Enter expression: "))
Data = [int(x) if x.isdigit() else x for x in expression]
unique_data=[]
for d in Data:
    if d not in unique_data:unique_data.append(d)
print(unique_data)