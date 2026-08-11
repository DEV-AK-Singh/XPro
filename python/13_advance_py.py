# nums = [1, 2, 3, 4, 5]

# # iterable
# for num in nums:
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# # iterator
# it = iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
# my_iterator = MyIterator([1, "some", 3, 4, 5])
# for item in my_iterator:
#     print(item)

# def my_generator():
#     print("Start of generator")
#     yield 1
#     print("Middle of generator")
#     yield 2
#     print("End of generator")
#     yield 3 
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen)) 

# lists = [x for x in range(10) if x % 2 == 0]
# gen = (x for x in range(10) if x % 2 == 0)
# # print(lists)
# # print(gen)
# for l in lists:
#     print(l)
# for g in gen:
#     print(g)

# with open("file.txt", "r") as file:
#     for line in file:
#         print(line)

# def load_dataset(filename):
#     with open(filename, encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()

# for line in load_dataset("file.txt"):
#     print(line)

# file_data = load_dataset("file.txt")
# print(next(file_data))
# print(next(file_data))
# print(next(file_data))

# def batches(data, batch_size):
#     for i in range(0, len(data), batch_size):
#         yield data[i:i + batch_size]
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for batch in batches(data, 3):
#     print(batch)

# def numbers(n):
#     for i in range(1, n + 1):
#         yield i
# def squares(nums):
#     for num in nums:
#         yield num * num
# def filter_even(nums):
#     for num in nums:
#         if num % 2 == 0:
#             yield num
# nums = numbers(10)
# squares = squares(nums)
# even = filter_even(squares)
# for num in even:
#     print(num)

# def calculator(): 
#     total = 0 
#     while True:
#         value = yield total
#         total += value
# calc = calculator()
# print(next(calc))
# print(calc.send(10))
# print(calc.send(20))
# print(calc.send(30))

# def example():
#     yield 1
#     yield 2
#     yield 3
#     return 4
# gen = example()
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen)) 

# import csv
# def load_rows(filename):
#     with open(filename, encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             yield row
# data = load_rows("file.csv")
# for row in data:
#     print(row)

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# # for name, age in zip(names, ages):
# #     print(f"{name} is {age} years old")
# # for i, name in enumerate(names):
# #     print(f"{i + 1}. {name}")
# is_adult = map(lambda age: age >= 18, ages)
# for name, is_adult in zip(names, is_adult):
#     print(f"{name} is {'adult' if is_adult else 'not adult'}")
# numbers = [1, 2, 3, 4, 5, 6]
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))