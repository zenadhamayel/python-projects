

#Assignment: Functions Intermediate II
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1.1Change the value 10 in x to 15
x[1][0]=15
print(x)
#1.2Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
print(students)
#1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)
#1.4 Change the value 20 in z to 30
z[0]['y']=30
print(z)
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
def iterateDictionary(some_list):
    for idx in range(len(some_list)):
        for key in some_list[idx]:
            print(key,'_',some_list[idx][key])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
#Get Values From a List of Dictionaries


def iterateDictionary2(key_name, some_list):
    for idx in range(len(some_list)):
        print(some_list[idx][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
#Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key  in some_dict:
        print(len(some_dict[key],),key.upper())
        for val in some_dict[key]:
            print(val)
        
        

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)









