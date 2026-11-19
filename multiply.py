col = int(input("enter a column: "))

for i in range(1, 16):
    for x in range(1, col + 1):
        print(i, "x", x, "=",i*x, end="\t")
    print()    
              