balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = 0.2/12
backup_balance = balance
lower = backup_balance/12
upper = (balance * (1 + monthlyInterestRate)**12)/12
epsilon = 0.03
monthlyPayment = 0
while abs(balance) > epsilon:
    balance = backup_balance
    monthlyPayment = (upper+lower)/2
    for i in range(12):
        balance -= monthlyPayment
        balance += monthlyInterestRate*balance
    if balance > epsilon:
        lower = monthlyPayment
    elif balance < epsilon:
        upper = monthlyPayment
    else:
        break
    

print(round(monthlyPayment,2))
