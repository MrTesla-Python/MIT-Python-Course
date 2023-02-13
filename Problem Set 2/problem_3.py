balance = 320000
annualInterestRate = 0.2
backup_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = backup_balance/12
upper = (backup_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    balance = backup_balance
    monthlyPayment = (upper+lower)/2
    for i in range(12):
        balance -= (monthlyPayment)
        balance += ((monthlyInterestRate)*balance)
    if balance > epsilon:
        lower = monthlyPayment
    elif balance < -epsilon:
        upper = monthlyPayment
    else:
        break
print(round(monthlyPayment, 2))