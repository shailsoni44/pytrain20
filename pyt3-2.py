print("\nQuestion 3\n")
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print(x[5][5][0])
print(x)

print("\nQuestion 4\n")
x=range(0,1000,1)
#y=xrange(1000) python 2 only
print(x)
#print(y[:25])

print("\nQuestion 5\n")
print("Tuples are immutable, so it reduces risk of losing data by overwritting or changing variable tye")

print("\nQuestion 6\n")
y=[]
for x in range(1,101):
    if x%6==0:
        y.append(x)
print(y)

print("\nQuestion 7\n")
x=str(input("Enter something: "))
print("Reserse string: ",x[::-1])
for i in range(0,len(x)):
    if x[i] in ['a','e','i','o','u']:
        print(x[i],"at",i ,"index")

print("\nQuestion 8\n")
x="hello my name is abcde"
y=x.split(" ")
for i in range(len(y)):
    if len(y[i])%2==0:
        print("Even letter words in the string are: ",y[i])


print("\nQuestion 9\n")
x=[1,2,3,4,5,6,7,8,9,-1]
for i in range(0,len(x)):
    for j in range(0,len(x)):
        if x[i]+x[j]==8 and i!=j:
            print("Numbers make total of 8 are:",x[i],"and", x[j])

print("\nQuestion 10\n")
even_list=[]
odd_list=[]
while len(even_list)<=4 or len(odd_list)<=4:
    x=int(input("Please enter number between 1 and 50: "))
    if x%2==0 and len(even_list)<=5:
        even_list.append(x)
    elif x%2!=0 and len(odd_list)<=5:
        odd_list.append(x)    
print("\nsum of first five entered even mumbers are=",sum(even_list),
    "\nmaximum of first five entered even numbers is=",max(even_list),
    "\nsum of first five entered odd mumbers are=",sum(odd_list),
    "\nmaximum of first five entered odd numbers is=",max(odd_list))

print("\nQuestion 11\n")
x=str(input("please enter something: "))
count={"a":0,"b":0,"c":0}
for i in range(len(x)):
    if x[i].isalpha():
        if str(x[i])=="a":
            count["a"]=count["a"]+1
        elif str(x[i])=="b":
            count["b"]=count["b"]+1
        elif str(x[i])=="c":
            count["c"]=count["c"]+1
print(count)

print("\nQuestion 12\n")
x=(1,2,3,4,5,6,7,8,9,10)
y=list()
for i in range(len(x)):
    if x[i]%2==0:
        y.append(x[i])
z=tuple(y)
print(z)