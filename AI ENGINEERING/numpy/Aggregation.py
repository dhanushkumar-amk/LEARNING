import numpy as np

a = np.array([1, 2, 13, 4, 5])

# sum of all elements
print("sum : ",np.sum(a))

# minimum element
print("minimum : ",np.min(a))

# maximum element
print("maximum : ",np.max(a))

# mean of all elements
print("mean : ",np.mean(a))

# median of all elements
print("median : ",np.median(a))

# standard deviation means how much the data is spread out from the mean
print("standard deviation : ",np.std(a))

# variance means square of standard deviation variance formula = sum of (x - mean)^2 / n example => (1-5)^2 + (2-5)^2 + (13-5)^2 + (4-5)^2 + (5-5)^2 / 5
print("variance : ",np.var(a))

# index of min and max means position of min and max
print("index of min : ",np.argmin(a))
print("index of max : ",np.argmax(a))
