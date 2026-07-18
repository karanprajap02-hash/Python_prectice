upper_limit = input("Enter the no for upper limit: ")
upper_limit_int = int(upper_limit)
arm_value = []

for num in range(1, upper_limit_int + 1):
    power = len(str(num))
    temp_num = num
    value_sum = 0
    
    while temp_num > 0:
        reminder_value = temp_num % 10
        value_sum += reminder_value ** power
        temp_num //= 10  
        
    if value_sum == num:
        arm_value.append(num)

print(f"Armstrong numbers up to {upper_limit}: {arm_value}")
