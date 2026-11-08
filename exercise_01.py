prices=[10, 20, 30, 40, 35, 45, 15, 65, 55, 50]
total_return = 0
highest_return = -1

for day in range(1,len(prices)):
    today = prices[day]
    yesterday = prices[day - 1]
    daily_return = (today - yesterday) / yesterday
    print("Daily Return:", round(daily_return * 100, 2), "%")
    total_return += daily_return
    if  daily_return > highest_return:
         highest_return = daily_return
           
    
print("Average return: ", round((total_return/(len(prices) -1)) * 100, 2), "%") 
# Why average misleads
average_return = total_return / (len(prices) - 1)
# Testing whtether the average return can be used to reconstruct the final price
print("Reconstructed price:", round(prices[0] * (1 + average_return) ** (len(prices) - 1), 2))

print("Highest Return:", round(highest_return * 100, 2), "%")

