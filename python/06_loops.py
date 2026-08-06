# for i in range(5):
#     print("Hello")

# for i in range(5, 10):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# name = "Python"
# for ch in name:
#     print(ch)

# student = {
#     "name": "Abhishek",
#     "age": 25,
#     "city": "Raipur"
# }

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, ":", value)

# colors = {"Red", "Green", "Blue"}
# for color in colors:
#     print(color)

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# lottery_numbers = [4, 8, 15, 16, 23, 42]
# while True:
#     my_numbers = int(input("Enter your lottery number: "))
#     if my_numbers in lottery_numbers:
#         print("You won!")
#         break
#     else:
#         print("Try again!")

# for i in range(1, 6):
#     if i == 3:
#         continue
#     if i == 4:
#         pass
#     if i == 5:
#         break
#     print(i)
# else:
#     print("Loop completed")

# for i in range(3):
#     for j in range(2):
#         print(i, j)

# languages = ["Python", "Java", "Go"]
# for index, language in enumerate(languages):
#     print(index, language)

# languages = ["Python", "Java", "Go"]
# for index, language in enumerate(languages, start=1):
#     print(index, language)

names = ["Alice", "Bob", "Charlie"]
marks = [90, 85, 95, 100]
print(zip(names, marks))
for name, mark in zip(names, marks):
    print(name, mark)