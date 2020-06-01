print("\nQuestion 1\n")
y=list(filter(lambda x:x%7==0 and x%3!=0 , range(1,100)))

print("List of",y)

print("\nQuestion 2\n")

def multi(n):
    return(n*n)
list_demo=[1,2,3,4]
out=list(map(lambda x:multi(x),list_demo))
print(out)

print("\nQuestion 3\n")

inp_str="eDx Course"
cap_letters=[i for i in inp_str if i.isupper()]
print(cap_letters)


print("\nQuestion 4\n")
Student = ['Smit', 'Jaya', 'Rayyan']    
capital = ['CSE', 'Networking', 'Operating System']

final={Student[i]:capital[i] for i in range(3)}

print(final)

print("\nusing zip function")
final={k:v for k,v in zip(Student,capital)}
print (final)


print("\nQuestion 6\n")

user = "Consultadd Training"
output = (user[-i] for i in range(1,(len(user)+1)))

for n in range(len(user)):
    print(next(output),end=" ")

print("\nQuestion 7\n")

def Hh(func):
    def wrapper(*args,**kwargs):
        print("before return")
        result = func (*args,**kwargs)
        print("after return")
        return result
        
    return wrapper

@Hh
def add4(i,j,k):
    return (4+i+j+k)

print(add4(5,6,7))
    