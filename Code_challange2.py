money = 7345

print("Current Money is,", money, "php")

Thousand = money // 1000
Thousand_change = money % 1000

FiveHundred = Thousand_change // 500
FiveChange = Thousand_change % 500

TwoHundred = FiveChange // 200
TwoChange = FiveChange % 200

OneHundred = TwoChange // 100
FiftyChange = TwoChange % 100

Fifty = FiftyChange // 50
TwentyChange = FiftyChange % 50

Twenty = TwentyChange // 20
TenChange = TwentyChange % 20

Ten = TenChange // 10
FiveChange = TenChange % 10

Five  = FiveChange // 5
OneChange = FiveChange % 5

One = OneChange // 1

print("1000 - ", Thousand)
print("500 -", FiveHundred)
print("200 -", TwoHundred)
print("100 -", OneHundred)
print("50 -", Fifty)
print("20 -", Twenty)
print("10 -", Ten)
print("5 -", Five)
print("1 -", One)