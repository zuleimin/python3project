import numpy as np

#b=np.random.seed(10)

b=np.random.randint(100,200,(3,4))

print(b)
c=np.sum(b, axis=None)
print(c)

