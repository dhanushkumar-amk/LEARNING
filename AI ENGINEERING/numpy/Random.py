
import numpy as np


 # random numbers between 0 and 1 (3 rows and 3 columns)
print(np.random.rand(3,3))

# random integers between 1 and 10 (3 rows and 3 columns)
print(np.random.randint(1,10))
print(np.random.randint(1,10 ,size=(3,3)))

# differnce btw normal, uniform and binomial distribution
# normal distribution => bell curve => bell curve means most of the values are around the mean
# uniform distribution => flat curve => flat curve means all the values are equally likely
# binomial distribution => discrete values => discrete values means only specific values are allowed

# normal distribution
print(np.random.normal(loc=50,scale=10,size=(3,3)))

# uniform distribution
print(np.random.uniform(low=0,high=10,size=(3,3)))

# binomial distribution
print(np.random.binomial(n=10,p=0.5,size=(3,3)))


