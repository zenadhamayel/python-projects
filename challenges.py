#basic Example Function:
#def add(a,b):
#    x=a+b
#    return x
#new_person=add(3,5)
#print(new_person)
#function with input parameter:IMPORTANT-Note:we consider name paramter,we consider zenad,ali arguments and pass them
def say_hi(name):
    print("Hi, " + name)
say_hi('zenad')
say_hi('ali') 
#a function call is equal to whatever that function returns.ex about return
def call(name):
    return 'Hi'+name
new_value=call("Hamdan")
print(new_value)
def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum1,sum2,sum3)
#ex:about list compersion
item=['appel','banana','Kiwi']
new_list=[]
for x in item:
    if "a" in x:
        new_list.append(x) 
print(new_list)
         



        



		

