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