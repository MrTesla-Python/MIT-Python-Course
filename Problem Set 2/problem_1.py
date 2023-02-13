# Test Case 1 
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance -= (monthlyPaymentRate*balance)
    balance += ((annualInterestRate/12)*balance)
    
print(round(balance, 3))