Name = input("Write your Name: ")

Item = input("Your name of Item:")

is_Fragile = bool(input("The Item is Fragile: "))

Weight = float(input("The Weight of Item:"))

Distance = float(input("The Distance of Item: "))

is_express = bool(input("The Item is Badly Needed:"))

is_international = bool(input("The Item is Ship Internationaly:"))

base_cost = weight*2.50 + distance*0.15

print("Sender Name: ", Name)
print("Name of Item: ", Item)

if is_Fragile == True :
    print("Fragile : yes")

print("Weight of Item: ", weight)        
print("The Distance: ", distance)

if is_express == True :
    print("Express: , Yes")
if is_international == True :
    print("International: , Yes")  
    
if weight >= 100 and weight <= 2:
    print("Total Shipping --> ", base_cost) 
    
elif is_express  == True and is_international == True : 
    print("Total = ", base_cost*1.40+50)

elif is_express == True or is_international == True and weight >= 20 :    
     print("Total = ", base_cost*1.20+25)

elif weight > 30 or distance > 1000:
    print("Total = ", base_cost+30)
    
else :
    print("Invalid")    


