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


