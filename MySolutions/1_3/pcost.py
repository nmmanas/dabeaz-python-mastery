file_name = '../../Data/portfolio.dat'

total_price = 0

with open(file_name) as file:

    for line in file:
            data = line.split()
            qty = int(data[1])
            price = float(data[2])
            total_price += qty*price

print(total_price)
