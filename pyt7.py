print("\nQuestion 1\n")

C=50
H=30
x=str(input("Please enter comma seperated variable D: "))
D=""
for i in (x.split(",")):
    D=D+i
print((2*C*float(D)/H)**0.5)


print("\nQuestion 2\n")

A=0

class shape:
    class square:
        def __init__(self,length):
            self.length=length

        def area(self):
            A = self.length**2
            return A
    def area(self,length,width):
        A = length*width
        return A

obshape=shape()
obsqr=shape.square(4)

A1=obshape.area(5,3)
A2=obsqr.area()
print("Area of ractangle with length 5 and width 3=",A1,"\nArea of sqare with length 4=",A2)


print("\nQuestion 3\n")

in_list=[-25,-10,-7,-3,2,4,8,10]
out_list=[]

class zero:
    def zerosum(self,l):
        for i in l:
            for j in l:
                if i!=j:
                    for k in l:
                        if j!=k and i!=k and i+j+k==0:
                            out_list.append([i,j,k])
                            l.remove(i)
                            l.remove(j)
                            l.remove(k)
        return out_list

obzero=zero()
print(obzero.zerosum(in_list))                


print("\nQuestion 4\n")

print("Part 1")
class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1

def main():
    b = Derived_Test()
    print("b.x",b.y)

main()

print("Child class does not take __init__ fuction properties from parent class", 
    "\n we must call super() function to inherit __init__ values")

print("Part 2")

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y

def main():
    obj = der()
    print(obj.x, obj.y)
main()

print("We called super().__init__() which copies init function from parent class. That's why we are seeing obj.x value")

print("Part 3")

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
 
    print(obj.x, obj.y)
main()

print("In class B when we called A.__init__(self,3) , it assigned value 3 to x", 
    "\n After that when we called count function of class b it increased value of y by 1 which initially was 0")


print("Part 4")

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i
class B(A):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i
obj = B()

print("super().__init__ calls init fuction of parent class and in this example it calls print(self.i)", 
    "\nInitially i is 15 but when passed through multiply function of class B i becomes 30")

    
print("\nQuestion 5\n")

class Time:
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min

    def addTime(self,a,b):
        outhr = self.hr + int(a)
        outmin = self.min + int(b)
        if outmin>=60:
            outmin-=60
            outhr+=1
        print("Total:",outhr,"hrs and",outmin,"mins")

    def DisplayMinute(self):
        print(60*self.hr + self.min,"mins")

ob=Time(2,50)
ob.addTime(1,20)
ob.DisplayMinute()


print("\nQuestion 6\n")


class Person:
        age=0
        b=0
        def __init__(self,a):
            self.ag=int(input("PLease enter your age:"))
            
                
        def age(self):
            if self.ag < 0:
                print("invalid age")
                self.a=self.age
                #exit()
            else:
                self.a=self.ag

        def amIOld(self):
            if self.a >= 0:
                if self.a < 13:
                    print("you are young")
                elif self.a <18:
                    print("you are teenager")
                else:
                    print("you are old")
            else:
                pass        
               
        def yearPasses(self):
            self.a += 1
            print("You will be",self.a,"years old in 1 years")

        

person=Person(0)
age=person.age()
year_1=person.yearPasses()
old=person.amIOld()

# blah blah blah


