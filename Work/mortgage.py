# mortgage.py
#
# Exercise 1.7
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
while principal > 0:
    months = months + 1
    if (months >= extra_payment_start_month) and (months <= extra_payment_end_month):
        add_payment = extra_payment
    else:
        add_payment = 0
    if principal * (1 + rate/12) - payment - add_payment > 0:
        principal = principal * (1 + rate/12) - payment - add_payment
        total_paid = total_paid + payment + add_payment
    else:
        total_paid = total_paid + principal
        principal = 0
    print(f'{months} {total_paid:0.2f}  {principal:0.2f}')
print('Total paid', total_paid)
print('Months', months)

