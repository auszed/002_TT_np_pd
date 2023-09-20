import numpy as np

# adding some exaples of numpy



'''
creation of arrays with specific or random numbers
'''
# explicitly add a type in a array
aaa = np.array([1, 2, 3, 4], dtype='float32')

# nested lists result in multidimensional arrays
bbb = np.array([range(i, i + 3) for i in [2, 4, 6]])

# Create a length-10 integer array filled with zeros
zeroos = np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with 1s
oness = np.ones((3, 5), dtype=float)


# Create a 3x5 array filled with 3.14
# filled by numers specifierd
number_specified = np.full((3, 5), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
number_espaciados = np.arange(0, 20, 2)


# Create an array of five values evenly spaced between 0 and 1
# numeros espaciados dictados por un numero 7
numero_separados = np.linspace(0, 1, 7)


# create random numbers
# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
random_numeros = np.random.random((3, 3))


# The probability density for the Gaussian distribution is
# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
random_normal_distr = np.random.normal(0, 1, (3, 3))

# Create random integers
# Create a 3x3 array of random integers in the interval [0, 10)
random_integers = np.random.randint(0, 10, (3, 3))



# Create a 3x3 identity matrix
identity_matrix =  np.eye(3)

# array([[ 1.,  0.,  0.],
# [ 0.,  1.,  0.],
#  [ 0.,  0.,  1.]])


# Create an uninitialized array of three integers
#  The values will be whatever happens to already exist at that
# memory location
emthy_values =  np.empty(5)


'''
================================
NumPy Array Attributes
================================

Determining the size, shape, memory consumption, and data types of arrays
'''
import numpy as np
np.random.seed(0)  # seed for reproducibility
# 1D array
x1 = np.random.randint(10, size=6)  # One-dimensional array
# 2D array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
# 3D array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

# for knowing the type
x3.dtype

# This attribute returns the size (in bytes) of each item (element) in the ndarray.
x3.itemsize

# This attribute returns the total number of bytes consumed by all the elements in the ndarray.
x3.nbytes


'''
================================
Indexing of arrays
================================


Getting and setting the value of individual array elements
'''

# 1D
x1[0]

# 2d
x2[0, 0]

# 3d
x3[0,2,5]


'''
================================
Slicing of arrays
================================
Getting and setting smaller subarrays within a larger array

'''

# formula
# x[start:stop:step]
x = np.arange(10)

x[::2]  # every other element


x[1::2]  # every other element, starting at index 1


x[5::-2]  # reversed every other from index 5


x2[:2, :3]  # two rows, three columns
'''
================================
Reshaping of arrays
================================
Changing the shape of a given array

'''

grid = np.arange(1, 17).reshape((4, 4))
print(grid)


# In NumPy, np.newaxis is a special keyword used to increase the dimension of the existing array by one more
# dimension. It's frequently used for reshaping arrays and for broadcasting purposes.
x[:, np.newaxis]



'''
================================
Joining and splitting of arrays
================================
Combining multiple arrays into one, and splitting one array into many


Concatenation, or joining of two arrays in NumPy, is primarily accomplished through the routines
- np.concatenate, 
- np.vstack, 
- np.hstack.
- np.concatenate 
takes a tuple or list of arrays as its first argument
'''

# joining the arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

# more then 2 arrays
z = [99, 99, 99]
print(np.concatenate([x, y, z]))

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
# muestra los array x encima de grid
np.vstack([x, grid])


# horizontally stack the arrays
y = np.array([[99],
            [99]])
np.hstack([grid, y])


# Similarly, np.dstack will stack arrays along the third axis.

# ==========
# spliting
# ==========

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

























