# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                total_cost = float(record['shares']) * float(record['price']) + total_cost
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)