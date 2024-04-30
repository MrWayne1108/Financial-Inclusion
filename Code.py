# Compound Interest Calculator

# Get input from user
principal_amount = int(input('Enter the principal amount: '))
rate_of_interest = int(input('Enter the rate of interest (in percent % ): ')) / 100
time_period = int(input("Number of times the interest is compounded per year: "))
no_of_years = int(input('Number of years: '))

# Calculate compound interest
final_amount = principal_amount * (1 + rate_of_interest / time_period) ** (time_period * no_of_years)

# Calculate simple interest
simple_interest_amount = principal_amount * (1 + rate_of_interest * no_of_years)

# Calculate amount saved using simple interest
amount_saved = final_amount - simple_interest_amount

# Print results
print(f'The final amount to be paid by you: {final_amount:,.2f}')
print(f'Amount to be paid using simple interest: {simple_interest_amount:,.2f}')
print(f'Amount saved using simple interest: {amount_saved:,.2f}')
