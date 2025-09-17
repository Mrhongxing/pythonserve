
import random
import numpy as np
arr=np.array([])
a=0
while a<16:
    c=random.random()
    a+=1
    arr=np.append(arr,10*c)
arr=np.reshape(arr,(4,4))
print(arr)