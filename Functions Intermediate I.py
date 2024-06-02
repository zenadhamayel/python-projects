import random
def randInt(min=0,max=100):
    if max<0:
        print("false max is bigger than 0")
    elif min>max:
        
        print("false max is bigger than min")
    else:
        if max !=100 and min !=0 :
            return round(random.random()*(max-min)+min) 
        if max !=100 :
            return round(random.random()*(max-0)+0)
        if min !=0 : 
            return round(random.random()*(100-min)+min)
        return round(random.random()*100)
print(f"return random number between 0 and 100 randInt={randInt()}") 
print(f"return random number between 0 and 100 randInt={randInt(max=50)}")
print(f"return random number between 0 and 100 randInt={randInt(min=50)}")
print(f"return random number between 0 and 100 randInt={randInt(min=50,max=500)}")