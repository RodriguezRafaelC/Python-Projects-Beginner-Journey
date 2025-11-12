loan_amount = eval(input("Enter loan amount : "))
loan_period = eval(input("Enter loan period : "))

loan_period  *= 12
principal = loan_amount / loan_period
balance = loan_amount
interest = 0

print("|    Month\t|    Monthlypayment\t|   Interest\t| Principal\t|    Remaining Loan  |")

for i in range(1, loan_period + 1, 1):
    balance -= principal
    interest = balance * 0.00256
    monthly = interest + principal
    print(f"|\t{i}\t{round(principal, 2)} \t\t{round(balance, 2)} \t{round(interest, 2)} \t{round(monthly, 2)}")