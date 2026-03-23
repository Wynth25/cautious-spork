#   <Task>
import random
schedule = []
for _ in range(1, 100):
	arrival = random.randint(0,1439)
	departure = random.randint(arrival+1,1440)
	schedule.append([arrival, departure])
#   </Task>

occ = 0
max = -1
for minute in range(0,1441):
	for train in schedule:
		if train[0] == minute:
			occ += 1
		if train[1] == minute:
			occ -= 1
	if occ > max:
		max = occ
print(max)
