def calculate_balance(principal, interest_rate_per_year, duration, number_of_payments):
    if interest_rate_per_year == 0:
        return principal-number_of_payments * (principal / (duration * 12.0) )   
    r = interest_rate_per_year/100/12.0
    n = duration * 12
    balance = principal * ((1.0 + r) ** n - (1.0 + r) ** number_of_payments) / (((1.0 + r) ** n) -1)
    return balance
