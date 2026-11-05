from getpass import getpass

u = "kingpogi"
p = "king123"

isLogin = False 

while isLogin == False:
    username = input("Enter your USERNAME ")
    password = input("Enter your PASSWORD ")

    if username == "kingpogi" and password == "king123":
        print("YEAHHHHHHH")
        isLogin == True
    else:
        print("OWWWW")
        isLogin == False    