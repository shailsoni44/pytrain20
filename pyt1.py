print("Question 1\n")

x= 1 ; y= 2.5 ; z='string'
print("Type of x:",type(x) , "\nType of y:", type(y) , "\nType of z:", type(z))

print("\nQuestion 2\n")

a=(1j+2) ; b = 3
print("Assigned value of a:", a,"\nAssigned value of b:",b)
a,b = b,a
print("After swapping value of a is:", a , "\nAfter swapping value of b is:", b)

print("\nQuestion 3\n")

a = 4 ; b = 5
print("Assigned value of a:", a,"\nAssigned value of b:",b)
x=a ; a=b ; b=x
print("After swapping value of a:", a,"\nAfter swapping value of b:",b)

#without using other variable
a=4 ; b = 5
print("Assigned value of a:", a,"\nAssigned value of b:",b)
a,b = b,a
print("After swapping value of a:", a,"\nAfter swapping value of b:",b)

print("\nQuestion 4\n")

print("for python 3+ \n v1 = eval (input('Please enter a value: ')) \n or v1 = input('Please eneter a value: ')")

print("For python 2\n v2 = input('Please enter the value: ')\n  which is same as \n  v2= eval(raw_input('Please enter the value: '))") 

print("\nQuestion 5\n")

x = int(input("Please enter two integer numbers between 1 and 10 \n First number is: "))
y = int(input("Second number is: "))
z = x+y
print("Total sum of the given numbers adding 30 into them:",z+30)

print("\nQuestion 6\n")

x= eval(input('Please enter any kind of data: '))
print("The input value data type is:",type(x))

print("\nQuestion 7\n")

helloWorld = "lower Camel case"
HelloWorld = "Upper camel case"
hello_world = "snake case"

print('we can write Hello world in',helloWorld,'like helloWorld' ,
    '\nwe can write Hello world in',HelloWorld,'like HelloWorld' ,
    '\nwe can write Hello world in',hello_world,'like hello_world')

print("\nQuestion 8\n")

print("Yes it will change value of a, Python is Dynamic language so it will take the latest value of a," ,
    "\nand every variable is free to have any data type")

