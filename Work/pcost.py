# pcost.py
#
# Exercise 1.27


# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row = line.split(',')
#         print(row)
#         shares = int(row[1])
#         price = float(row[2])
#         total_cost += shares * price
#
# print('Total cost is', round(total_cost, ndigits=2))

def portfolio_cost(filename):
    total_cost = 0.0
    ctr = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            ctr += 1
            row = line.split(',')
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print('ValueError at row', ctr)

        return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost is', cost)