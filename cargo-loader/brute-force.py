#   <Task>
import random

package_weights = random.choices(range(1,30), k=20)
max_weight = sum(random.choices(package_weights, k=3))
packages = []
for i in package_weights:
    packages.append([i, int(i*5*random.random())])
print(f"Maximum cargo capacity: {max_weight}")
print(f"Available packages:")
for index, item in enumerate(packages):
    print(f"Package {index+1}: 	Weight –  {item[0]}, 	Value – {item[1]}")
#   </Task>

