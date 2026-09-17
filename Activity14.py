age = int(input("Enter Your AGE ---> "))

is_employed = bool(input("Are you employed? True/False --> "))

credit_score = int(input("Enter your CREDIT SCORE ---> "))

annual_income = float(input("Enter your ANNUAL INCOME ---> "))

has_collateral = bool(input("Do you have collateral? True/Falase ---> "))

base_interest = 0.0

if age >= 21 and is_employed == True:
    print("Access Approved")

    if credit_score >= 750:
        print("You have a  High Credit")  
        if annual_income >= 10000:
            base_interest = 4.5
        else :
            base_interest = 5.0
        print("You are approves", base_interest)       
         
    elif credit_score >= 600:
        print("You have fair credit score")   
        if has_collateral:
            base_interest = 7.0
        elif annual_income < 40000:
            base_interest = 9.5
        else:
             base_interest = 8.0
        print("You are approved", base_interest)
    else:
         print("Rejected credit score to low")       
         
else:
    print("Rejected: Fails baseline criteria")         
    
           
           