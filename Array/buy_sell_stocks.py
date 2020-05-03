"""Solution of finding profit from buying and selling stocks"""


# Approach - 1 : Using Brute Force
def buy_and_sell_once(stock_prices):
    max_profit = 0
    for i, _ in enumerate(stock_prices):
        for j in range(i + 1, len(stock_prices)):
            if stock_prices[j] - stock_prices[i] > max_profit:
                max_profit = stock_prices[j] - stock_prices[i]

    return max_profit

# Time Complexity: O(n^2)
# Space Complexity: O(1)


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(f"Max profit by the brute force is: {(buy_and_sell_once(A))}")


# Approach 2 - Keeping track of minimum price
def buy_and_sell_2(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)


print(f"Max profit by keeping track of minimum price is: \
{(buy_and_sell_2(A))}")
