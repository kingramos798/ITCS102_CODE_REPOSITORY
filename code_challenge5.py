size = int(input("Input the size number "))

for x in range(5):
    for y in range(5):
        if x == y or x + y == size -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()            