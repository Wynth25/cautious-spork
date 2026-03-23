## The Cargo Loader

# The Scenario

You are writing the loading software for a last-mile delivery van. The van has a strict maximum weight limit. You have a queue of packages waiting to be loaded. Each package has a specific weight and a delivery fee (value) that the company earns for delivering it. Your goal is to pack the van to maximize the total delivery fees earned without snapping the van's axles.

#The Input

Your Python function will receive the van's ```max_weight``` (an integer) and a list of ```packages```. Each package is represented by a list containing its weight and its value: ```[weight, value]```.
```max_weight = 50```
```packages = [[10, 60], [20, 100], [30, 120], [15, 70]]```

# The Rules of the System

The Physical Realm: You cannot exceed the ```max_weight``` of the van.

All or Nothing: You cannot split a package in half. You either load the whole box, or you leave it on the dock (this is why this is called a 0/1 problem).

Limited Stock: You only have exactly one of each package in the list.

Your Objective
Write a Python function ```def calculate_max_cargo(max_weight, packages):``` that returns:

# The maximum possible delivery value you can fit in the van.

The exact list of packages you chose to load.

# Example Test Case

```
Python
Input: 
max_weight = 50
packages = [[10, 60], [20, 100], [30, 120], [15, 70]]

Expected Output:
Max Value: 230
Packages Loaded: [[10, 60], [20, 100], [15, 70]]

# Breakdown:
# If you grab the heaviest/most valuable package [30, 120], you only have 20 weight left. 
# You could add [20, 100] for a total value of 220.
# BUT, if you ignore the 30kg package and take the 10kg, 20kg, and 15kg packages, 
# they weigh exactly 45kg and give you a higher total value of 230!
```