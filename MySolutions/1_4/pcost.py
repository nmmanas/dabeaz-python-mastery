def portfolio_cost(filename):
    total_price = 0
    with open(filename) as file:

        for line in file:
                data = line.split()
                try:
                    qty = int(data[1])
                    price = float(data[2])
                    total_price += qty*price
                except ValueError as e:
                    print("Couldn't parse:", repr(line))
                    print("Reason:", e)
    return total_price

file_name = '../../Data/portfolio3.dat'
total_price = portfolio_cost(file_name)
print(total_price)
