# expression =input("Enter expression: ").split(" ")
# data = [int(x) if x.isdigit() else x for x in expression]
# def count_freq(data):
#     freq_items={}
#     for items in data:
#         freq_items[items]=freq_items.get(items,0)+1
#         # get reset to spesific value when items no present
#     print(f"frequency of elements:\n {freq_items}")
# count_freq(data)

# second approch
expression =input("Enter expression: ").split(" ")
datas = [int(x) if x.isdigit() else x for x in expression]
def counts_freq(datas):
    freq_items={}
    for items in datas:
        if items not in freq_items:
            freq_items[items]=1
        else:
            freq_items[items]=freq_items[items]+1
            
    print(f"frequency of elements:\n {freq_items}")


counts_freq(datas)