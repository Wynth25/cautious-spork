#   <Task>
import random
prices = []
prices = random.choices (range(1,101), k=24)
for i in range(0, len(prices)):
    print(f"{i}:00 - {i}:59 – {prices[i]}") 
#   </Task>

def calculate_max_profit(prices):
    method = []
    b = 0
    profit = 0

    for i in range(len(prices)):
        if i == len(prices)-1:
            if b == 0:
                method.append("HOLD")
            else:
                method.append("SELL")
                profit += prices[i]
        
        elif prices[i] > prices[i+1] and b == 1:
            method.append("SELL")
            b-=1
            profit += prices[i]
        
        elif prices[i] < prices[i+1] and b == 0:
            method.append("BUY")
            b+=1
            profit -= prices[i]
        
        else:
            method.append("HOLD")

    print(f"The maximum profit is: {profit}")
    print(method)
    


calculate_max_profit(prices)
