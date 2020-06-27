import random

def primt(obj):
    print(obj)
    
def cheemsify(obj,count_m = 2):
    if not isinstance(obj,str):
        raise TypeError("the input type must be a string")

    new_obj = obj
    for _ in range(count_m):
        l = len(new_obj)
        insert_pos = random.randrange(1,l)
        new_obj = new_obj[0:insert_pos] +'m' + new_obj[insert_pos:l] 

    return new_obj


    
