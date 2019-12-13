"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Entmy.jucer sales: $"))
while sales <= 0:
    print("Value cannot be negative or zero")
    sales = float(input("Enter sales: $"))


if sales < 1000:
    sales = sales * float(0.10)
    print("additional bonus is", sales ,"!")
elif sales >= 1000:
    sales = sales * float(0.15)
    print("additional bonus is", sales ,"!")
