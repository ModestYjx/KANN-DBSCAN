import numpy as np
a = [1,2,3,4,5]
a = np.array(a)
print(a)
print("--------")
x = np.tile(a,(len(a),2))
y = x.T
print(x)
print("--------")
print(y)