def func(num):
    
    arr_of_num = [0]
    
    for x in num:
        if x % 2 == 0:
            arr_of_num.append(x)

    return arr_of_num

print(func(9))
