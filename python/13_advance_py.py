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