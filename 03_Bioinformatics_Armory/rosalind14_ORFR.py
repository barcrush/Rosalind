def my_func(i):
    if i ==0:
        return
    else:
        i = i - 1
    print(i)
    my_func(i)
    my_func(i)

print(my_func(4))