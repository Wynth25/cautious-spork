#   <Task>
import random
schedule = []
for _ in range(1, 100):
	arrival = random.randint(0,1439)
	departure = random.randint(arrival+1,1440)
	schedule.append([arrival, departure])
#   </Task>

occ = [0]*1440
for train in schedule:
    for minute in range(train[0], train[1]):
        occ[minute] += 1

print(f"The required number of platforms is {max(occ)}.")
print(f"Peak minute first appears  at minute {occ.index(max(occ))}.")
