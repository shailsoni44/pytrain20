
print("\nQuestion 1\n")
x=str(input("please enter something: "))
print(x[::-1])

print("\nQuestion 2\n")
a=str(input("please enter input: "))
def x(j):
    capi=0
    small=0
    for i in range(len(a)):
        if a[i].isupper() :
            capi=capi+1
        elif a[i].islower():
            small=small+1
    print("No. of upper case characters:", capi,
        "\nNo. of lower case characters:", small)
x(a)

print("\nQuestion 3\n")
li=["a","b","c","c","d",'b',"e","e","a"]
def x(i):
    b=set(i)
    c=list(b)
    print(c)
x(li)

print("\nQuestion 4\n")
in1=str(input("please enter input: "))
def x(i):
    a=i.split("-")
    a.sort()
    b=str()
    for j in a:
        if j==a[0]:
            b=j
        else:
            b=b+"-"+j
    print(b)
x(in1)

print("\nQuestion 5\n")
in1=str(input("Please enter input: "))
print(in1.upper())

print("\nQuestion 6\n")
in1=input("please enter a number: ")
in2=input("please enter another number: ")
def x(a,b):
    #print(type(a),type(b))
    print((int(a)+int(b)))
x(in1,in2)

print("\nQuestion 7\n")
in1=input("Please enter input 1: ")
in2=input("Please enter input 2: ")
def longstr(x,y):
    if len(x)==len(y):
        print('\nLength of both string are same: ',x,'\n',y)
    elif len(x)>len(y):
        print('\nLength of first string is greater: ',x)
    else:
        print('\nLength of second string is greater: ',y)
    
longstr(in1,in2)

print("\nQuestion 8\n")
def sqr(a):
    b=[]
    for i in range(1,a+1):
        b.append(i**2)
    print("Square of 1 to 20 integeres as tuple is:",tuple(b))
sqr(20)

print("\nQuestion 9\n")
def even_odd(a):
    for i in range(a+1):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
even_odd(11)

print("\nQuestion 10\n")
x=range(1,21)
y=filter(lambda x: x%2==0,list(x))
print(list(y))

print("\nQuestion 11\n")
x=[1,2,3,4,5,6,7,8,9,10]
y=list(map(lambda x:x**2,list(filter(lambda x:x%2==0,x))))
print(y)

print("\nQuestion 12\n")
x=5
y=0
def div(a,b):
    try:
        print(a/b)
    except:
        print("Denominator can't be zero")
div(x,y)

print("\nQuestion 13\n")
from functools import reduce
lis=[[1,2,3],[4,5],[6,7,8]]
y=reduce(lambda x,y:x+y,lis)
print(y)
z=map(str,y)
w=str(reduce(lambda x,y:x+y,z))
print(w)

print("\nQuestion 14\n")
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

def a():
    try:
        f(x, 4)
    except:
        print("Function f was not defined")
    finally:
        print('after f')
    print('after f?')
a()





