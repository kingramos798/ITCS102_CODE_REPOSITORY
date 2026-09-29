owner_age = int(input("Enter your Age: "))
monthly_revenue = float(input("Your Monthly Revenue: "))
credit_score = int(input("Enter your CC: "))
years_in_business = float(input("Years in Business: "))
has_defaults = bool(input("You have Defaults? True/False: "))
collateral_name = str(input("Enter CN: "))
collateral_value = float(input("Enter CV: "))

max_loan = 0.0
base_fee = 0.0

if owner_age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("You are Qualified")
    if credit_score >= 720: #Tier1
        max_loan =  3 * monthly_revenue
        print("HIGH CREDIT SCORE")
        if monthly_revenue >= 50000:
            print("Revenue Higher than 50k")
            max_loan = base * 0.015
        else:
            print("Revenue Lower than 50k")
            max_loan = base_fee * 0.025
            print("base fee rate", base_fee)

        if collateral_value >= max_loan:
            print("Collateral", collateral_name, "with a value of", collateral_value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for", collateral_name)

        surge_fee_rate = max_loan * base_fee
        if max_loan % 500 != 0:
            print("addotional charge added")
            surge_fee_rate += 250
            print("Updated base fee is", base_fee)
        

    elif 620 <= credit_score < 720:
        print("Your Higher Range")
        max_loan = monthly_revenue * 1.5
        print("Maximum Loan is", max_loan)
        if years_in_business >= 5.0:
            print("Business is more than 5yrs")
            base_fee = max_loan * 2.0
        else:
            print("Business is less than 5yrs")
            base_fee = max_loan * 3.5
            print("Base fee rate", base_fee)  

    else:
        print("Invalid")
else:
    print("Baseline Failed")                
                






