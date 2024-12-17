import numpy as np

multiples = np.empty((0, ))
for x in range (1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        multiples = np.append(multiples, x)

print(int(np.sum(multiples)))
