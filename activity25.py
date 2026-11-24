def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x+1):
            print("*", end=" ")
        print()


def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if x == 0 or y == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()           

def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact    

print(my_factorial(4))

box(5)
box(20)


def sum(x, y):
    return x+y

taga_triangle(5)
taga_triangle(8)
taga_triangle(3)
taga_triangle(4)

print(sum(35, 5))
print(sum(48, 3)* 40)