#Basic - Print all integers from 0 to 150.
#for int in range(0,151,1):
#    print(int)
#Print all the multiples of 5 from 5 to 1,000:
#for i in range(5, 1001): 
#    if i % 5 == 0: 
#        print(i) 
#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#for i in range(1,101,1):
#    if i % 5 == 0:
#        print("coding")
#    if i % 10 == 0:
#        print(" coding Dojo") 
#Add odd integers from 0 to 500,000, and print the final su
#minimum = 0
#maximum = 500000
#Oddtotal = 0

#for number in range(minimum, maximum+1):
#    if(number % 2 != 0):
#        print("{0}".format(number))
#        Oddtotal = Oddtotal + number

#print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))
#Print positive numbers starting at 2018, counting down by fours.
#def count_dec  ():
#    num=2018
#    while num>0:
        
#        print(num)
#       num=num-4
             
#count_dec  ()
#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def count(lowNum ,highNum,mult):
    for i in range(lowNum,highNum):
        if i % mult == 0 :
            print(i)
count(2 ,9,3)            