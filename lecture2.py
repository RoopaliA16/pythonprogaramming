# concept of print function

# f- string 

# %% 
name = 'roopali'
age = 30 
salary = 22

print(f'hiii my name is {name}and my age is {age} and salary is {salary}')


# %%


# concept of .format method

print('hiii my name is {} and my age is {} and salary is {}'.format ( name, age, salary))
 
# concept of list 

lst1 = []
lst2 = [1,2,3,56.78,"hiii","world",True,False,[10,20,30],(100,200,300),{1,2,3,},{"india":1000},None]

# concept flow 

# if condition 

name = input(" enter your name :")

if name == "roopali":
    print(f"your name is {name}")



coin_side = input("enter the coin side :")

if coin_side.lower() == "head":
    print("you win the game")

else:
    print("you lose the game")   


# %%
# concept of indexing and slicing 

str = "welcome to the world of python programming" 
str = "hello world"
print(str[4])
print(str[-5])


# %% 

print(str1[-6:-2])

# str[start:stop:step]

# %% 
print(str1[ : : 2])

'''
question :
write a program to print whether the value entered by user is palindrome or not 

logic :

1. ask user to enter a string 
2. reverse the string 
3. compare the original string with the reversed string 
4. if both are same then it is palindrome otherwise it is not palindrome 

'''

# %%

string = input("enter a string :")
string1 = string[::-1]  # str1 [start:stop:step] : ----> -1 means reverse the string 

if string == string1:
    print(f"{string}is a palindrome")
else:
    print(f"{string}is not a palindrome")
    










