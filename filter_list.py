def filter_list(l):
    return [a for a in l if type(a)!=str]

print(filter_list([1,2,'a','b']))