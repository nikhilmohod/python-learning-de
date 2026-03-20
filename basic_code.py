#Basic mommand For starting 
print("Basic Python 3.*.*")
print("step 1st : .pyc file (bytecode)", "step 2nd : PVM interepreter", sep='\n')
print(''' multi line staement ''')
print('Variable Practice :')

first_name = "nikhil"
last_name = "mohod"

num_x = 10

print(first_name +  last_name + str(num_x)) # sate data type

print("multi assingment")

x,y,z=5,15,20
print(x,y,z,sep='\n')

print("multi assingment same value")

x = y  = z=25
print(x,y,z,sep='\n')

print("Indentation")

is_true = False
if(is_true):
    print("condition work")
else:
    print("condition not work")

print("type casting")
a = 10
b = "10"
c= True
print(type(str(a)) ,type(int(b)) , type(int(c)))
print(str(a) ,int(b) , int(c))

dummy_str = "we are learning python"
print(dummy_str[0], dummy_str[:2], dummy_str[2:], dummy_str[-10:], sep='\n')

print("string operation")

print(dummy_str.replace("r","$"))

print(dummy_str.split(" "))

print(dummy_str.endswith("n")) #bool output

print(dummy_str.count("r"))

print("is num",dummy_str.isnumeric())

dummy_num = "10"
print("is num", dummy_num.isnumeric()) # input string required but i will gives inside the string quote