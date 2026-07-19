print("IT IS PRASHANT 'S TRIANGLE AREA CALCULATOR :") 
a=float(input("give me first side length of triangle:"))
b=float(input("give me second side length of triangle:"))
c=float(input("give me third side length of triangle:"))

s=(a+b+c)/2

print("semi perametre:",s)

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("area is:",area)

if a>b+c:
  print("it not make a triangle please check the values!")
if b>a+c:
    print("it not make a triangle please check the values!")
if c>a+b:
    print("it not make a triangle please check the values!")
if area==0:
    print("it not possible!\nPlease!check values.\nThank you!")