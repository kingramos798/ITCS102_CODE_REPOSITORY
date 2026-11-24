from activity25 import taga_triangle
from activity25 import sum
from activity25 import box
from activity25 import my_factorial 
import os

while True:
    print("MINI MENU")
    print("SELECT OPTION: ")
    print("1 - taga tringle")
    print("2 - sum")
    print("3 - box")
    print("4 - factorial")
    print("5 - EXIT")
    choose = int(input("Select Option --> "))

    if choose == 1:
        os.system('cls')
        print("taga_triangle")
        size = int(input("Enter the size: "))
        taga_triangle(size)
        continue
    elif choose == 2:
        os.system('cls')
        print("Sum: ")
        num1 = int(input(" number 1 -> "))
        num2 = int(input(" number 2 -> "))
        print(f"the sum {num1} and {num2} is {sum(num1, num2)}")
        continue
    elif choose == 3:
        os.system('cls')
        print("BOX")
        size = int(input("size of box -> "))
        box(size)
        continue
    elif choose == 4:
        os.system('cls')
        print("FACTORIAL")
        num = int(input("enter a any number -> "))
        print(f"The factorial of {num} is {my_factorial(num)}")
        continue
    elif choose == 5:
        print("system exit")
        break
    else:
        print("Error")