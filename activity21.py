sum = 0

BRTBRT = True
while BRTBRT == True:
    yaks = int(input("Enter a number "))

    if yaks == 0:
        print("The Loop Terminated")
        print("Total of all sum", sum)
        break
    else:
        print("Continue Loop")
        sum += yaks
        print("Current Total is", sum)
        continue
