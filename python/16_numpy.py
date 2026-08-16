# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# li = [1, 2, 3, 4, 5]
# print(li)
# print(type(li))
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr.shape)
# print(arr.dtype)
# new_arr = np.array([x * 2 for x in arr])
# print(new_arr)

# execution time check
# import numpy as np
# import timeit
# Pass the code snippet as a string
# statement = "-".join(str(n) for n in range(100))
# Measures execution time for 10,000 iterations
# execution_time = timeit.timeit(stmt=f'"{statement}"', number=10000)
# li = [1, 2, 3, 4, 5]
# execution_time_1 = timeit.timeit(stmt=f'"{2 * li}"', number=100000)
# arr = np.array([1, 2, 3, 4, 5])
# execution_time_2 = timeit.timeit(stmt=f'"{2 * arr}"', number=100000)
# print(f"Execution time: {execution_time_1:.8f} seconds, {execution_time_2:.8f} seconds")

# l1 = [1, 2, 3]
# l2 = [4, 5, 7]
# print(l1 + l2)

# import numpy as np
# ar1 = np.array([1, 2, 3, 4, 5])
# ar2 = np.array([6, 7, 8, 9, 10])
# ar3 = np.arange(1, 11)
# print(ar1)
# print(ar2)
# print(ar3)
# ar4 = ar1 + ar2
# print(ar4)
# ar5 = ar1 * ar2
# print(ar5)
# ar6 = ar1 - ar2
# print(ar6)
# ar7 = ar1 / ar2
# print(ar7)
# ar8 = ar1 // ar2
# print(ar8)
# ar9 = ar1 % ar2
# print(ar9)
# ar10 = ar1 ** ar2
# print(ar10)

# import numpy as np
# ar_range = np.arange(1, 11)
# print(ar_range)
# ar_zero = np.zeros(5)
# print(ar_zero)
# ar_one = np.ones((2, 3))
# print(ar_one)
# ar_empty = np.empty((2, 3))
# print(ar_empty)
# ar_full = np.full((2, 3), 5)
# print(ar_full)
# ar_eye = np.eye(4)
# print(ar_eye)
# ar_diag = np.diag([1, 2, 3, 4])
# print(ar_diag)
# ar_diag1 = np.diag([1, 2, 3, 4], k=1)
# print(ar_diag1)
# ar_diag2 = np.diag([1, 2, 3, 4], k=-1)
# print(ar_diag2)
# ar_diag3 = np.diag([1, 2, 3, 4], k=2)
# print(ar_diag3)
# ar_linspace = np.linspace(0, 10, 5)
# print(ar_linspace)

# # rand, randn, ranf, randint
# import numpy as np  
# import math
# # ar_rand = np.random.rand(5)
# ar_rand = np.array([math.floor(x * 10) for x in np.random.rand(5)]) 
# print(ar_rand)
# ar_randn = np.random.randn(5)
# print(ar_randn)
# ar_randf = np.random.ranf(5)
# print(ar_randf)
# ar_randint = np.random.randint(1, 10, (5, 5))
# print(ar_randint)

# import numpy as np
# x1 = np.array([1,2,3,4])
# x2 = x1.astype(np.float64)
# print(x1, x1.dtype)
# print(x2, x2.dtype)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])

# arr_1 = arr + 3 // np.add(arr, 3)
# print(arr_1)
# arr_2 = arr - 3 // np.subtract(arr, 3)
# print(arr_2)
# arr_3 = arr * 3 // np.multiply(arr, 3)
# print(arr_3)
# arr_4 = arr / 3 // np.divide(arr, 3)
# print(arr_4)
# arr_5 = arr // 3 // np.floor_divide(arr, 3)
# print(arr_5)
# arr_6 = arr % 3 // np.mod(arr, 3)
# print(arr_6)
# arr_7 = arr ** 3 // np.power(arr, 3)
# print(arr_7)
# arr_8 = 1 / arr // np.reciprocal(arr)
# print(arr_8)

# arr_9 = np.max(arr)
# print(arr_9, np.argmax(arr))
# arr_10 = np.min(arr)
# print(arr_10, np.argmin(arr))
# arr_11 = np.mean(arr)
# print(arr_11)
# arr_12 = np.median(arr)
# print(arr_12)
# arr_13 = np.std(arr)
# print(arr_13)
# arr_14 = np.var(arr)
# print(arr_14)

# arr_15 = np.array([[1,5,3], [7,9,8], [4,5,6]])
# print(arr_15)
# arr_16 = np.sum(arr_15)
# print(arr_16)
# arr_17 = np.sum(arr_15, axis=0) # 0 - columns
# print(arr_17)
# arr_18 = np.sum(arr_15, axis=1) # 1 - rows
# print(arr_18)
# arr_19 = np.sqrt(arr_15)
# print(arr_19)
# arr_20 = np.sort(arr_15, axis=None)
# print(arr_20)
# arr_21 = np.cumsum(arr_15)
# print(arr_21)

# Broadcasting in Numpy means that you can perform operations between arrays of different shapes.
# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([[1],[2],[3]])
# print(arr1+arr2)

# Indexing in Numpy means that you can access elements of an array using a single index.
# import numpy as np
# arr1 = np.array([1,2,3,4,5])
# print(arr1.shape)
# print(arr1.ndim)
# arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2.shape)
# print(arr2.ndim)
# arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# print(arr3.shape)
# print(arr3.ndim)
# print(arr1[2])
# print(arr2[1,2])
# print(arr3[1,:1,:])