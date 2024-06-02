#count positive part2:
def count_positives(array):
    count=0
    for val in array:
        if val>0:
            count+=1
    array[len(array)-1]=count
    return array
print([-5,-9,0,32,-6,22])
print(count_positives([-5,-9,0,32,-6,22]))
#Example: sum_total([1,2,3,4]) should return 10
def Sumoflist(array):
    total=0
    for val in array:
        
            total+=val
    return total
print(Sumoflist([1,2,3,4]))
print(Sumoflist([6,3,-2]))
#Example: average([1,2,3,4]) should return 2.5
def avglist(lst,low=0,high=100):
    for i in range(low,high):
        avg=sum(lst)/len(lst)
    return avg
print(avglist([1,2,3,4]))
#average([1,2,3,4]) should return 2.5
def list(lst,low=0,high=100):
    for i in range(low,high):
        length=len(lst)      
    return length 
print(list([37,2,-19]))
print(list([]))
#Example: minimum([37,2,1,-9]) should return -9
def list(lst,low=0,high=100):
    for i in range(low,high):
        length=lst.sort()
    return length    
list = [37,2,1,-9]

print( min(list))
#Example: maximum([37,2,1,-9]) should return 37
def list(lst,low=0,high=100):
    for i in range(low,high):
        length=lst.sort()
    return length    
list = [37,2,1,-9]

print( max(list))
 
