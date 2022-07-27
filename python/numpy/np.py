import numpy as np
import random

print(np.array([1,2,3], dtype=np.float))
print(np.arange(1,10,2))
print(np.array(range(1,10,2)))
print(np.round(np.array([random.random() for i in range(10)]), 2))
