# Approch 1

lists=[int(x) for x in input("Enter the no:").split(",")]
def sec(lists):
    if len(lists) < 2:
        return None
    print(sorted(set(lists))[-2])
sec(lists)

# Approch 2

def get_second_largest(nums):
    if len(nums) < 2:
        return None

    largest = second_larg = float('-inf')  # Initialize to negative infinity
    
    for num in nums:
        if num > largest:
            second_larg = largest
            largest = num
        elif num > second_larg and num !=largest:
            second = num
            
    return second_larg if second_larg != float('-inf') else None

print(get_second_largest([lists]))
