# report.py
#
# Exercise 2.4

import csv
import sys
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            temp = {}
            temp['name'] = record['name']
            temp['shares'] = int(record['shares'])
            temp['price'] = float(record['price'])
            portfolio.append(temp)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices

def make_report(portfolio, prices):
    report = []
    for i in portfolio:
        single_stock = (i['name'], i['shares'], prices[i['name']], prices[i['name']]- i['price'])
        report.append(single_stock)
    return report


#if len(sys.argv) == 2:
#    filename = sys.argv[1]
#else:
#    filename = 'Data/portfolio.csv'

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
header = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
separator_single = '-' * 10
total_separator = ''
for i in range(len(headers)):
    total_separator = total_separator + ' ' + separator_single
print(header)
print(total_separator)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')