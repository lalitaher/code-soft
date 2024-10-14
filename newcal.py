# calculator

a=int(input("Enter the number="))
b=int(input("Enter the number="))
c=a+b
d=a-b
e=a*b
f=a/b
print("press 1 for addition\npress 2 for substraction\npress 3 for multiplication\npress 4 for division")

choice=int(input("enter your choice bet 1-4:="))
if(choice==1):
    print(c)
elif(choice==2):
    print(d)
elif(choice==3):
    print(e)
elif(choice==4):
    print(f)
else:
    print("invalid choice enter")
