"""
Write A Program to implement PDA 

"""
from  stack import Stack

print("PDA Language")


inString  = input("Enter A string of a's and b's e.g aabbab : ")

print(f"Give String is : {inString}")

mystack  = Stack(len(inString))


print("In Values     Is Equal         My Stack")
for alpha in inString:
    if alpha == 'a':
        mystack.push(alpha)

    else:
        mystack.pop()

    print(f" {alpha}             {mystack.isEmpty()}           {' '.join(mystack.stack)}")


if mystack.isEmpty():
    print("a's and b's are Equal")
else:
    print("a's and b's are Not Equal")


