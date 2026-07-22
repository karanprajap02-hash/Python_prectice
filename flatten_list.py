matrix=[[1,2],[3,4],[5,6]]
flat_lst=[items for sublst in matrix for items in sublst]
print(f"Flatten list: {flat_lst}")

# also use 
def flate(matrix):
    for items in matrix:
        if isinstance (items,matrix):
            yield from flate(items)
        else:
            yield items

new_lst=flate(matrix)
print(new_lst)