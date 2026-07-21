
numbers = [x for x in input("Enter mathematical expression (separate by space and higher order first): ").split(" ")]

value = []
symbols = []

# Use enumerate to get both the index (i) and the actual item (num)
for i, num in enumerate(numbers):
    if i % 2 == 0:
        # Even indexes (0, 2, 4...) hold the numbers/values
        value.append(int(num))
    else:
        # Odd indexes (1, 3, 5...) hold the mathematical symbols
        symbols.append(num)

# Print the final categorized lists
# print(f"s {symbols}")
# print(f"v {value}")
result=value[0]
for i,s in enumerate(symbols):
    next_value=value[i+1]
    if s=='/':
        result//=next_value
    elif s=='*':
        result*=next_value
    elif s=='+':
        result+=next_value
    elif s=='-':
        result-=next_value
print(f"result: {result}")


# ,,,,
import re

# This regular expression extracts all numbers and operator symbols automatically
expression = re.findall(r'\d+|[+\-*/]', input("Enter expression: "))
# print(expression)

value = [int(x) if x.isdigit() else x for x in expression]

# This puts numbers and symbols in one list: [1, '+', 2, '*', 3]

# 2. Pass 1: Multiplication and Division
i = 0
while i < len(value):
    if value[i] in ['*', '/']:
        left = value[i-1]
        op = value[i]
        right = value[i+1]
        
        # Calculate
        if op == '*': 
            res = left * right
        else: 
            res = left // right
        
        # Replace the three items (left, op, right) with the result
        value[i-1:i+2] = [res]
        # Stay at the same index to check for consecutive operators
        i -= 1
    i += 1

# 3. Pass 2: Addition and Subtraction
result = value[0]
i = 1
while i < len(value):
    op = value[i]
    right = value[i+1]
    
    if op == '+': result += right
    elif op == '-': result -= right
    i += 2

print(f"Result: {result}")
