from functools import reduce


print("function")

def add_cal( x, y):
    add = x+y
    print(add)
    return add

add_cal(5,7)

def add_cal_more( x, y,z=10):
    add = x+y+z
    print(add)
    return add

add_cal_more(5,5,2)

def add_cal_asstric( *x): # tuple
    add = x
    print(add)
    return add

add_cal_asstric(1,1,2)

def add_cal_asstric( **x): # tuple
    add = x
    print(add)
    return add

add_cal_asstric(x=1,y=1,z=2)


print("lambda function") # min function no complex

addition = lambda x,y : x+y
print(addition(10,20))

print("Map , Filter ,Reduce")

val_list = [2,3,4,5,6,7]

def add(val):
    return val+val

print(list(map(add,val_list)))


print(" Filter ")
val_list = [2,3,4,5,6,7]

def add(val):

    if val != 5:
        return val+val

# due to this filter condition with map we will get none for file valu result.
#coz map call ech value and share with function
#filer eleminate this None value
print(list(filter(add,val_list)))


print(" Reduce ")
val_list = [2,3,4,5,6,7]

def add(val,val_1):
    return val+val_1

# it will take 1st and 2nd value from list
# continuosly doin same on all list
# condition not allowed reduc the list
print(reduce(add,val_list))


print("exception handling")

try: # main code
    a.pop()
    print("try")

except Exception as e: # on error
    print(e)

finally : # always run
    print("final")

# custome "raise" error us for custom error 1. TypeError , ValueError , Exception
# raise Exception("msg")

print("global var")

def global_val():

    global a 
    a = 10

global_val()
print(a)