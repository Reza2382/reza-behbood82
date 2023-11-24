x=int(input("Enter x="))
y=int(input("Enter y="))
s=x+y
print("s=",s)

print()

x=int(input("Enter x="))
y=int(input("Enter y="))
if(x>y):
    print("x is bigger than y")
elif(y>x):
    print("y is bigger than x")
else:
    print("equal")

print()

x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))
max=x
if(y>x):
    max=y
if(z>x):
   max=z
print("max=",max)

print()

x=int(input("Enter 1st number="))
count=1
while count<100:
    number=int(input("Enter another number="))
    count+=1
    if(number>x):
       max=number
print(max)

print()

x=int(input("Enter 1st number="))
max=x
min=x
count=1
while count<100:
    number=int(input("Enter number="))
    if(number>max):
        max=number

    elif(number<min):
        min=number
    count+=1

print(max)
print(min)

print()


lst=[]
for i in range(1,11):
    lst.append(int(input("Enter value:")))

lst.sort(reverse=True)
print(lst)


print()

lst=[]
for i in range(1,101):
    lst.append(int(input("Enter value:")))

lst.sort()
print(lst)


print()


x=int(input("Enter x="))
if(x%2==0):
    print("The number is even")
else:
    print("The number is odd")


print()

num=int(input("Enter number="))
max=num
for i in range(1,10):
    x=int(input("Enter another number="))
    if(x>max):
        max=x

print(max)


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
for i in range(a+1,b):
    if(i%2==0):
        print(i)


print()


n=int(input("Enter n="))
flag=True
for i in range(2,n):
    if(n%i==0):
        flag=False
        break

if(flag):
    print("F")

else:
    print("H")


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
count=0
if a>b:
    (a,b)=(b,a)

for i in range(a+1,b):
    for j in range(2,i):
        if(i%j==0):
            count+=1
            break
        if(count!=0):
           print(i)
           break


print()


a=int(input("Enter a="))
b=int(input("Enter b="))
if(a>b):
    (a,b)=(b,a)

for i in range(a+1,b):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=i
        if(sum==2*i):
            print(i)


print()


n=int(input("Enter number="))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
   print('True')

else:
   print("False")


print()


lst=[]
for i in range(1,101):
    lst.append(int(input("Enter value=")))
print(max(lst))


print()


lst=[]
for i in range(1,11):
    lst.append(int(input("Enter value=")))
x=int(input("Enter x="))
if x in lst:
    print("found")
else:
    print("not found")



print()



lst1=[]
lst2=[]
for i in range(1,101):
    lst1.append(int(input('enter value=')))
for j in range(1,101):
    lst2.append(int(input('Enter more values=')))
c=lst1+lst2
print(c)



print()


x=int(input("Enter x="))
sum=0
while x>=0:
    x=int(input('Enter x='))
    sum+=x

print(sum-x)



print()



x=int(input("Enter x="))
f=1
i=1
while i<=x:
    f*=i
    i+=1
print("factorial=",f)


print()


m=int(input("Enter m="))
n=int(input("Enter n="))
fact=1
while m>n:
    f=m-n
    for i in range(1,f):
        fact*=i

print("factorial=",fact)


            



























