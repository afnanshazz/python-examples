"""*****"""
"""*****"""
"""*****"""
"""*****"""
"""*****"""
for value in range(0,5):
    print("*****")

"""12345"""
"""12345"""
"""12345"""
"""12345"""
"""12345"""
for value in range(0,5):
    print("12345")

input1=int(input("enter a value"))
input1
for value in range(input1):
    print("12345")

'''
* * * * *  
* * * *  
* * *  
* *  
*'''

for value in range(5,0,-1):
    print(value*'*')
"""*
**
***
****
*****"""
for value in range(0,6,1):
    print(value*'*')

input2=int(input("enter a value"))
input2
for value in range(input2):
    print(value*'*')
"""1
12
123
1234
12345"""
for value in range(0,6,1):
    print(value*'*',end=' ') 
      
for row in range(1,7):
    for col in range(1,row):
        print(col,end='')
    print()    
"""12345
1234
123
12
1"""          
for row in range(7,1,-1):
    for col in range(1,row):
        print(col,end='')
    print()    