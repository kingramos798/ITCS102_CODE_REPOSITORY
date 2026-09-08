import getpass

username = 'KingPogi'

password = 'password'

u = input('Input Username --->')

p = getpass.getpass('Input Password --->')

if username == u and p == password :
            print("Acces Granted")

else:
           print("Access Denied")