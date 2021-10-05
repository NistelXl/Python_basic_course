# Задание 5
# Пункт 1

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]


for i in range(len(prices)):
    prices[i] = float(prices[i])
    prices[i] = "{0:.2f}".format(prices[i])
    prices[i] = str(prices[i]).split('.')

    for item in range(0, len(prices[i]), 2):
        print(prices[i][item], 'руб', end = " ")
    for item in range(1, len(prices[i]), 2):
        print(prices[i][item], 'коп,', end=" ")



# Пункт 2

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print(id(prices))

prices.sort()
print(prices)

print(id(prices))

# Пункт 3

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

prices.sort()
prices_reversed = list(reversed(prices))
print(prices_reversed)

# Пункт 4
#
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

prices.sort()
print(prices[-5:])