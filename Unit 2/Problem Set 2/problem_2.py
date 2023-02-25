# Test Case 1
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 10
test_bal = balance
while monthlyPayment < balance:
    for i in range(12):
        test_bal -= (monthlyPayment)
        test_bal += ((monthlyInterestRate)*test_bal)
    
    if test_bal <= 0:
        break
    else:
        test_bal = balance
        monthlyPayment+=10
print(monthlyPayment)
