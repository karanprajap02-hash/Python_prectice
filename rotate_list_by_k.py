k=int(input("Enter the value of k: "))
lst=input("Enter the data in list: ").split(",")
def rotate_by_k(lst,k):
    if not lst:return
    k%=len(lst)
    # if k is greater then len of list 
    return lst[k:]+lst[:k]
new_lst=rotate_by_k(lst,k)
print(f"new list:{new_lst}") 
