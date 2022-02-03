import random
num1 = int(input("first number"))
num2 = int(input("second number"))
option = int(
    input("select1 for addition,2 for subtraction, 3 for multiplication"))


def procedure1(num1, num2):

    sum = num1+num2
    print(sum)


def procedure2(num1, num2):
    diff = num1-num2
    print(diff)


def procedure3(num1, num2):
    multi = num1*num2
    print(multi)


if option == 1:
    procedure1(num1, num2)
elif option == 2:
    procedure2(num1, num2)
elif option == 3:
    procedure3(num1, num2)

else:
    print("not correct option")
