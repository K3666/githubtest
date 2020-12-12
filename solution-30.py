# Your function for calculating payment goes here
def calculate_payment(principal, interest_rate_per_year, duration):
    if interest_rate_per_year==0:
        return principal/(duration * 12)
    r = interest_rate_per_year/100/12
    n = duration * 12
    montly_payment = principal * (r * ((1.0 + r) ** n)) / (((1.0 + r) ** n) -1)
    return montly_payment
# Your function for calculating remaining balance goes here
def calculate_balance(principal, interest_rate_per_year, duration, number_of_payments):
    if interest_rate_per_year == 0:
        return principal-number_of_payments * (principal / (duration * 12.0))   
    r = interest_rate_per_year/100/12.0
    n = duration * 12
    balance = principal * ((1.0 + r) ** n - (1.0 + r) ** number_of_payments) / (((1.0 + r) ** n) -1)
    return balance
# Your main program goes here
principal = float(input("Enter loan amount :"))
annual_interest_rate = float(input("Enter annual interest rate (percent): "))
duration = int(input("Enter loan duration in years: "))    
monthly_payment = calculate_payment(principal, annual_interest_rate, duration)
print('LOAN AMOUNT:',int(principal),'INTEREST RATE (PERCENT):', int(annual_interest_rate))
print('DURATION (YEARS):',duration,'MONTHLY PAYMENT:',int(monthly_payment))
for year_number in range(1,1 + duration):
    y = calculate_balance(principal, annual_interest_rate, duration, year_number*12)
    print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment * year_number * 12))
