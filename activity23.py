slamdunk = []
detective_conan = []
one_punch_man = []
sports = []
action = []

while True:
    ans = input("You watch ANIME?").lower()
    if ans == "yes":
        print("what kind of anime you watch?")
        print("1 - slamdunk \n2-detective_conan\n3-one_punch_man\n4-sports\n5-action")
        choice = int(input("input "))
        if choice == 1:
            print("Slamdunk")
            title = input("Enter the ANIME title")
            slamdunk.append(title)
            print("list")
            print(slamdunk)
