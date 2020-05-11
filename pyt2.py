print("Question 1\n")
print("Please enter a number, enter -1 to stop")
while True:
    y=int(input("Please enter a number: "))
    if int(y/3) == (y/3) and int(y/5) == (y/5):
        print("Consultadd Python Training")
    elif int(y/3) == (y/3):
        print("Consultadd")
    elif int(y/5) == (y/5):
        print("c")
    elif y==-1:
        break
    else:
        continue

print("\nQuestion 2\n")
print("Please choose number from following",
    "\n1 for Addition of two numbers", "\n2 for Subtraction of two numbers",
    "\n3 for Multiplication of two numbers", "\n4 for Division of two numbers", 
    "\n5 for Average of 4 numbers", "\n-1 to stop")

while True:
    O=int(input("Please select your operation: "))
    if O==-1:
        break
    elif O not in [1,2,3,4,5]:
        print("please select Appropriate number from 1 to 5")
        continue
    a=float(input("Select your first number: "))
    b=float(input("Select your second number: "))
    if O==1:
        print("Addition of given numbers=",a+b)
        if (a+b)<0:
            print("NEGATIVE")
    elif O==2:
        print("Subtracting second number from first number=",a-b)
        if (a-b)<0:
            print("NEGATIVE")
    elif O==3:
        print("Multiplication of given numbers=",a*b)
        if (a*b)<0:
            print("NEGATIVE")
    elif O==4:
        print("Division of first number by second number=",a/b)
        if (a/b)<0:
            print("NEGATIVE")
    elif O==5:
        c=float(input("Select your third number: "))
        d=float(input("Select your fourth number: "))
        print("Average of given four numbers=",((a+b+c+d)/4))
        if ((a+b+c+d)/4)<0:
            print("NEGATIVE")

print("\nQuestion 3\n")
a=10 ; b=20 ; c=30
avg=(a+b+c)/3
print("Avg =",avg)
if avg>a and avg>b and avg>c:
    print("Avg is higher than a,b,c")
elif avg>a and avg>b:
    print("Avg is higher than a,b")
elif avg>a and avg>c:
    print("Avg is higher than a,c")
elif avg>b and avg>c:
    print ("Avg is higher than b,c")
elif avg>a:
    print("Avg is just higher than a")
elif avg>b:
    print("Avg is just higher than b")
elif avg>c:
    print("Avg is just higher than c")
else:
    print("All values are equal")

print("\nQuestion 4\n") 

while True:
    n = int(input("Please enter a number: "))
    if n>=0:
        print("Good Going")
    else: break
print("It's Over")

print("\nQuestion 5\n") 
a=2000
while a<=3000:
    if int(a/7)==(a/7) and int(a/5)!=(a/5):
        print(a)
    a=a+1

print("\nQuestion 6\n") 
print("First code will result in error as x is not list so in operator can not be used")
# x=123 
# for i in x:
#     print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("\nQuestion 7\n")
i=0
while i<=6:
    if i==3 or i==6:
        i=i+1
        continue
    print(i)
    i+=1

print("\nQuestion 8\n")
a=str(input("Please enter text: "))
l=0
d=0
n=0
while n<len(a):
    try:
        int(a[n])
        d=d+1
    except:
        l=l+1
    n=n+1
print("Letters =",l ,"\nDigits =",d)

print("\nQuestion 9\n")
number= 334
answer=None
while True:
    if answer==None:
        answer=input("Guess the lucky 3 digit number: ")
        if int(answer)==number:
            break
    else:
        print("Do you still want to guess again? enter no to stop or guess new number")
        answer=input("Answer: ")
        try:
            if int(answer)==number:
                break
        except:
            if str(answer)=="no":
                break

print("\nQuestion 10\n")
counter=1
number=445
while counter<=5:
    print("Type in the",counter,"number")
    x=int(input())
    counter=counter+1
    if x==number:
        print("Good Guess!")
    else: print("Try Again!")
print("Game Over!")

print("\nQuestion 11\n")
counter=1
number=445
while counter<=5:
    print("Type in the",counter,"number")
    x=int(input())
    counter=counter+1
    if x==number:
        print("Good Guess!")
        break
    elif counter!=6 : 
        print("Try Again!")
    else:
        print("Sorry but that was not very successful")

