unpaidBalance = balance

monthlyInterestRate = (annualInterestRate / 12.0)

lower = round(balance / 12.0, 2)
higher = round((balance * (1 + monthlyInterestRate) ** 12) / 12.0, 2)
lowestPayment = round((lower + higher) / 2, 2)

found = False

while found == False:

    for i in range(0, 12):
        # print("Balance beginning of month:", round(unpaidBalance, 2))
        unpaidBalance -= lowestPayment
        # print("Balance end of month:", round(unpaidBalance, 2))
        unpaidBalance = round(unpaidBalance + ((annualInterestRate / 12.0) * unpaidBalance), 2)

    if unpaidBalance > 0:
        # this would mean the new lowestPayment should be higher
        lower = lowestPayment
        lowestPayment = (lower + higher) / 2
        # print("New lowestPayment is", lowestPayment)
        unpaidBalance = balance
    elif unpaidBalance < 0:
        # this would mean the new lowestPayment should be lower
        higher = lowestPayment
        lowestPayment = (lower + higher) / 2
        # print("New lowestPayment is", lowestPayment)
        unpaidBalance = balance
    else:
        print("Lowest payment:", round(lowestPayment, 2))
        found = True
