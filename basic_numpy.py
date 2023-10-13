import numpy as np  # importing numpy

a1 = np.array([1, 2, 3])  # declaration
type(a1)  # to know the data type.
a1.shape  # to know the shape of the array
a1.ndim  # to know the dimension of the array
a1.dtype  # to know the data type more clearlly like dtype('int64')
a1.size  # to know the size.number elements in the array
ones = np.ones(
    (3,), dtype=int
)  # it return the array of ones with defined shap and dtype
# ones take the 3 arguments first mention the shape, second mention the dtype, and third mention the order
zeros = np.zeros((2, 3), dtype=int)  # it will return the array of zeros
range_array = np.arange(
    0, 9, 1, float
)  # it will also return the array starts with zero, ends with 9-1, and with step 1
# arange will takes 4 arguments start,end,step,dtype.
random_array = np.random.randint(
    0, 10, size=(3, 5)
)  # it will return the array with shape (3,5) elements from 0 to 9
random_array = np.random.random(
    (5, 3)
)  # it will return the array with mentioned shape elements start with 0.0 to 0.1
np.random.seed(
    seed=1
)  # np.random.ramdom() will ganarates the random numbers every time we run.But the need is generate random numbres with defined shape but don't change them every time you run the code
# that random array stick to the seed.if you change the seed then array will changes until you change the seed.
a1[0]  # indexing in 1D array
print(a1[:1])  # slicing in 1D array
a2 = np.random.randint(0, 99, size=(5, 5))  # a2 is 2D array
print(a2[0:2])  # sclicing an multi-dimension array
print(a2[0][0])  # indexing in multi-dimension array

# Manipulating & comparing arrays

a = np.array([1, 2, 3])
print(a + a1)  # we can add two arrays with same dimension, same shape, and same size


# Aggregation
np.mean(a1)
np.min(a1)
np.max(a1)
np.std(a1)
np.var(a1)
