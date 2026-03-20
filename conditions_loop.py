print("conditions and loops")
is_val = True
num = 25

if(not is_val):
    print("if block")
elif((is_val) & (num == 25)): #carefull for condition braces
    print("elif block")
    if(num > 10):
        print("if block")
else:
    print("else block")


print("for loop")

dummy_arr = [10,20,30,40,50]

for i in dummy_arr:
    print("arr value :",i)

for i in range(1,5):
    print("range arr value :",i)


for i in range(1,5):
    print("range arr value :",i)
    if(i==4):
        print("break :",i)
        break # break the loop
        continue # continue the loop


print("for while")

while(len(dummy_arr) >  2):
    print("while :",dummy_arr[1])
    break

print("extra avd")

all_files = ["data1.csv", "image.png", "data2.csv", "readme.txt"]
            #[{Output Expression} {for Item in List} {if Condition} ]
csv_files = [file for file in all_files if file.endswith(".csv")] # 1st loop run - 2nd single value condition check 
print(csv_files) 
