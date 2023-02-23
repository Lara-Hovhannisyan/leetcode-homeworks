prices = list(map(int, input("Enter a list of prices, separated by commas: ").split(",")))

profit = 0
for i in range(len(prices)):
    lowest_day_index = prices.index(min(prices[i:]))
    highest_day_index = prices.index(max(prices[lowest_day_index:]))
    if prices[highest_day_index] > prices[lowest_day_index]:
        profit = max(profit, prices[highest_day_index] - prices[lowest_day_index])
    else:
        continue
print(profit)


