#The Energy Arbitrage Engine
**The Scenario**
You are writing the core decision-making algorithm for a day-ahead electricity trading system. Prices fluctuate wildly throughout the day based on demand and renewable energy generation. Your system controls a virtual battery, and your goal is to maximize Total Profit (PnL).

**The Input**
Your Python function will receive a list of integers. Each integer represents the price of electricity (in EUR) for a specific hour of the day.
prices = [10, 22, 5, 75, 65, 80, 15, 35]

**The Rules of the System**

Capacity: You have a battery that can store exactly 1 unit of energy.

Starting State: You start the day with an empty battery and 0 EUR in profit.

Actions: Every hour, you can make exactly one choice: BUY, SELL, or HOLD.

State Restrictions: * You cannot BUY if the battery is already full.

You cannot SELL if the battery is empty.

Unlimited Trades: You can buy and sell as many times as you want throughout the day to keep accumulating profit, as long as you respect the battery capacity.

**Your Objective**
Write a Python function def calculate_max_profit(prices): that evaluates the day's prices and returns two things:

The maximum possible profit you can make in that period.

A list of the exact actions taken each hour to achieve that profit.
