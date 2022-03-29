from operating_overload import *

op1 = Operating_Overloading()
op2 = Operating_Overloading()

op1.accept()
op2.accept()

while True:
        ch = int(input("1.Add\n2.Sub\n3.Mul\n4.FloorDiv\n 0.Exit\n"))
        if(ch==1):
            op1+op2
        elif(ch==2):
            op1-op2
        elif(ch==3):
            op1*op2
        elif(ch==4):
            op1//op2
        else:
            break
