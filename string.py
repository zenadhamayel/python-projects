#The following is a list of commonly used string methods:
#EX1:
x = "Allah Akbar"
print(x.title())
#EX2:about Tuples
name=('zenad','hamayel',16,'false')
print(name[0])
#ex3:list 
empty_list =[]
ninjas=['Rozen','KB','oliver']
print(ninjas[2])
ninjas[0]='france'
ninjas.append('Michel')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)
#common-type of function:
print(type(2.63))		
print(type('new_person'))	
#function to know length:
print(len('new_person'))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11
#Type Casting or Explicit Type Conversion:(this way to add string to num)
print("Hello world" +  str(42) )
#ex:about another ex to add string to num
total=40
user="5"
print(total+int(user))
#conditional_statement:
x=55
if(x>10):
    print("x bigger than 10")
elif(x>50):
    print("x bigger than 50")
else:
    print("x smaller than 10")


#loops in range nunbers:
for x in range (0,10,1):
    print(x)
for x in range (0,10):    
    print(x) 
for x in range (10):
    print(x)
#loops through list:
#my_list = ["abc", 123, "xyz"]
#for i in range(0, len(my_list)):
#    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
my_list = ["abc", 123, "xyz"]
for v in my_list:
    print(v)
#EX: FOR loops through dictionaries (output key):
my_dict={"zenad":"huge","hamayel":"big","ali":"small"}
for k in my_dict:
    print(k)
#EX: FOR loops through dictionaries (output value of key):
my_dict={"zenad":"huge","hamayel":"big","ali":"small"}
for k in my_dict:
    print(my_dict[k]) 
#Ex:Dictionaries also have a few additional methods that allow us to iterate through them
my_dict={"France":"paris","Japan":"Tokyo","palestine":"Jerasalum"}
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key,value in  my_dict.items():
    print(key,"",value) 
#loops:
for count in range(0,5):
    print("looping - ", count)
#same statement but in while:
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#Break statement:when some external condition is triggered, requiring a hasty exit from a loop.
for val in "string":
    if val == "i":
        break
    print(val)

#continue statement:
for val in "string":
    if val == "i":
        continue
    print(val)



















