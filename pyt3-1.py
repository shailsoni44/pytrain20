print("\nQuestion 1\n")
a = [1,2,(3j+4), 4.7, "consultadd",6,7,8,9,10]
print(a)

print("\nQuestion 2\n")
b=a[:5]
print(b)

print("\nQuestion 3\n")
x=[2,3,4,5,6,7,8]
total=0
mult=1
for n in x:
    total=total+n
    mult=mult*n
print("sum=",total,"\nmultiplication=",mult)

print("\nQuestion 4\n")
print("largest value of set x=",max(x),"\nsmallest value of set x=",min(x))

print("\nQuestion 5\n")
for n in x:
    if (n%2==0):
        x.remove(n)
print(x)

print("\nQuestion 6\n")
a=range(1,31)
s=[]
for i in a:
    s.append(i**2)
x=s[:5]
x.extend(s[-5:])
print(x)

print("\nQuestion 7\n")
a=[1,3,5,7,9,10]
b=[2,4,6,8]
a.pop(-1)
a.extend(b)
print(a)

print("\nQuestion 8\n")
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

print("\nQuestion 9\n")
x={}
n=int(input("please enter a number: "))
for i in range(1,n+1):
    x[i]=i*i
print(x)

print("\nQuestion 10\n")
n=input("please enter numbers seperated by comma: ")
l=n.split(",")
t=tuple(l)

print(t,"\n",l )