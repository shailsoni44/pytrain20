print("\nQuestion 1\n")
x=None
y=0
def s1():
    try:
        1+1==3
    except SyntaxError:
        print("please check the code again")
s1()

print("\nQuestion 2\n")
from sys import argv
progname, filename = argv

try:
    x=open(filename,"r")
    y=x.read()
    print(y)
    x.close()
    print("file closed")
except:
    print("Please enter correct name: ")
    filename=input()

print("\nQuestion 3\n")

x=int(input("Please enter 4 digit number: "))
try:
    if len(str(x))!=4:
        raise ValueError ("Please length is too short/long !!!"
         ,"Please provide only four digits")
    else:
        print("Good number")
        
except ValueError:
    print("Please length is too short/long !!!"
         ,"Please provide only four digits")
    



print("\nQuestion 4\n") 

n=0
x=input("Please enter your email id: ")
y=input("Please enter your password: ")
z=""

while n<3 and y!=z:
    if n==0:
        z=input("Please re-type your password ")
        n+=1
    else:
        
        print("Password do not match please try again")
        z=input("Please re-type your password ")
        n+=1

if y!=z:
    print("Please reload the browser to try again")
else:
    print("Account created successfully")


print("\nQuestion 6\n") 

with open("doc.txt",'r') as fh:
    fr=fh.read()
    fx=fr.split()

    for i in fx:
        if len(i)%2==0:
            print(i)
        
 


