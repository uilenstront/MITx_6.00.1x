# annualInterestRate = 0.2
monthlyInterestRate = (annualInterestRate / 12.0)
# monthlyPaymentRate = 0.04
# balance = 484

for i in range(0, 12):
    # print("Month", i, "remaining balance:", round(balance, 2))
    minimumMonthlyPayment = round((balance * monthlyPaymentRate), 2)
    # print("Month", i, "minimum payment:", minimumMonthlyPayment)
    balance = round((balance - minimumMonthlyPayment), 2)
    # print("Month", i, "unpaid balance:", balance)
    interest = round((monthlyInterestRate * balance), 2)
    # print("Month", i, "interest:", interest)
    balance += interest

print("Remaining balance:", round(balance, 2))