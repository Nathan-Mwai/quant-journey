# Lesson 1: Variables, lists and loops
# Lines starting with # are comments. Python ignores them; they are notes for humans.

# The prices below are made up for practice. They are not real market data.

# A VARIABLE is a name attached to a value.
stock_name = "Practice Stock"  # text is called a "string"
shares_owned = 250             # a whole number is an "int"
buy_price = 28.50              # a decimal number is a "float"

# We can calculate with variables.
cost = shares_owned * buy_price
print("Stock:", stock_name)
print("Total cost in KES:", cost)

# A LIST holds many values in order. These are five days of closing prices.
prices = [28.50, 29.10, 28.80, 30.00, 30.60]

# Positions start counting at 0, not 1. This catches everyone out at first.
# A position of -1 counts from the end, so it means the last value.
print("First price:", prices[0])
print("Last price:", prices[-1])
print("Number of days:", len(prices))

# You know this formula from economics:
#   return = (today's price - yesterday's price) / yesterday's price
#
# A LOOP repeats the indented lines, once for each value.
# range(1, 5) gives 1, 2, 3, 4. We start at 1 because day 0 has no yesterday.
print("\nDaily returns:")
for day in range(1, len(prices)):
    today = prices[day]
    yesterday = prices[day - 1]
    daily_return = (today - yesterday) / yesterday
    print("Day", day, "return:", round(daily_return * 100, 2), "%")

# Return over the whole period, and what the position is worth now.
total_return = (prices[-1] - prices[0]) / prices[0]
current_value = shares_owned * prices[-1]
print("\nTotal return:", round(total_return * 100, 2), "%")
print("Position value in KES:", current_value)
print("Profit in KES:", round(current_value - cost, 2))
