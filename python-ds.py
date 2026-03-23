print("Python Data structure")

print("list / array")
arr_list = [20,30,"data","val",[1,2,3]]

print("main : ",arr_list[3])
print("internatl : ",arr_list[4][2])
print("main : ",arr_list[-3:]) #  arr_lis( len(arr_lis )-3 : len(arr_lis ))

arr_list2 = [20,30,"data","val",1,2,3]
print("arr_list2 : ",arr_list2[1:5:2]) # start : end : iteration / jump

print("more methods")

arr_list3 = [20,30,"data","val",1,2,3]

arr_list3.append("new ele")
print("arr_list3 : ",arr_list3)
arr_list3.insert(2,"new ele-2") # add new one in given posision
print("arr_list3 : ",arr_list3)

arr_list3.pop() # for last value
print("arr_list3 : ",arr_list3)

arr_list3.pop(2) # for index
print("arr_list3 : ",arr_list3)

arr_list3.remove("data") # direct value
print("arr_list3 : ",arr_list3)




new_list = [1,2,3,4,5,6,7,8,9]

print("using : ",new_list[::-1]) # minus 1 from curecnt location so start from last by default
#print("using 1: ",new_list[::-1])

for i in reversed(new_list):
    print(i)

# list with condition and epression
new_list_1 = [i * i for i in new_list if i > 3]
print("new_list_1" ,new_list_1)


# list with condition and epression
new_list_2 = [i  for i in new_list if i > 3 if i!=7]
print("new_list_2" ,new_list_2)

print("disctionary") # key vvalu pair

new_dictionary = {"x":1,"y":2,"z":3}
print("before new_dictionary",new_dictionary)
new_dictionary["x"] = 4
print("after new_dictionary",new_dictionary) # update val;ue of x to 4
new_dictionary.pop("z")
print("after new_dictionary",new_dictionary) #  remove key z

print("after new_dictionary",new_dictionary.items()) # iterable tupple

for key ,value in new_dictionary.items():
    print(key ,value)

# List comprehension vaprun complex data filter karne
# pune_users = [info['name'] for user_id, info in users_data.items() if info['city'] == "Pune"]

# print(f"Pune Users: {pune_users}")

print("set")
a = set()
a = {1,2,3,4,5,3,4,2}
b = {1,3,4}

print(a.union(b))
print(a.intersection(b))
a.remove(2) 
a.add(20)
print(a)


print("tuple") # ()

new_tuple = (1,2,3,4)
print(new_tuple)
new_tuplelist = list(new_tuple)
print(new_tuplelist)
new_tuplelist.append(10)
new_tuplelist_1 = tuple(new_tuplelist)
print(new_tuplelist_1)