for i in range(6, 0, 1):
    for x in range(1, i+1):
        print(" ", end=" ")
        for c in range(1, 7 - i):
            print(c, end=" ")
        for a in range(5-i, 0, -1):
            print(a, end=" ")
    print()             