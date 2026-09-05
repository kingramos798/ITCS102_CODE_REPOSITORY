#contentation = combining strings

hobbies = ""

h = input("What are your hobbies -->") 
hobbies += h + ", "

h = input("Any other?") 
hobbies += h +  ", "

h = input("What hobbbies are you love the most?")
hobbies += h + ", "

print("So, my hobbies are", hobbies)