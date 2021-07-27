########################
## Generator Function ##
########################

def even_int_func(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    
    return result

results = even_int_func(10)

## will print out the integers ##
print(results)


##############################
## Returns Generator Object ##
##############################

def even_int_func_obj(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

results_obj = even_int_func_obj(10)

## will print out the generator object ##
print(results_obj)
## will print out the integers ##
print(list(results_obj))

