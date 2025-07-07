monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))
monthlySaving = monthlyIncome - monthlyExpenses
annualInterest = 0.05

projectedSavings = int((monthlySaving * 12) + (monthlySaving * 12 * annualInterest))

print("Your monthly savings are $" + str(monthlySaving))
print("Projected savings after one year, with interest, is: " + "$" + str(projectedSavings))
