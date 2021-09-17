# balance = 3926.00
unpaidBalance = balance
# annualInterestRate = 0.2

lowestPayment = 10.0
monthlyInterestRate = (annualInterestRate / 12.0)

found = False

while found == False:
    for i in range(0, 12):
        # print("Balance beginning of month:", round(unpaidBalance, 2))
        unpaidBalance -= lowestPayment
        # print("Balance end of month:", round(unpaidBalance, 2))
        unpaidBalance = unpaidBalance + ((annualInterestRate / 12.0) * unpaidBalance)

    if unpaidBalance <= 0:
        print("Lowest payment:", int(lowestPayment))
        found = True
    else:
        lowestPayment += 10.0
        unpaidBalance = balance
