# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# with open('file.txt', 'r') as file:
#     content = file.read()
# print(content)

# with open('file.txt', 'r') as file:
#     content = file.read(7)
# print(content)

# with open('file.txt', 'r') as file:
#     content = file.readline()  
# print(content)

# with open('file.txt', 'r') as file:
#     content = file.readlines()  
#     for line in content:
#         print(line)

# with open("file.txt", "w") as file:
#     # file.write("Hello Python")
#     file.writelines(["Hello Python\n", "Hello World\n", "Hello AI\n"])

# from pathlib import Path
# path = Path("file.txt")
# print(path.read_text())
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())

# from pathlib import Path
# data_dir = Path("../python")
# for file in data_dir.iterdir():
#     print(file.name)

# import json
# data = {
#     "name": "Abhishek",
#     "age": 25,
#     "skills": ["Python", "AI", "ML"]
# }
# with open("user.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4)

# import json
# data = {
#     "name": "Abhishek",
#     "age": 25,
#     "skills": ["Python", "AI", "ML"]
# }
# json_string = json.dumps(data)
# print(json_string)

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv
# rows = [
#     ["Alice", 22, 90],
#     ["Bob", 24, 85],
#     ["Charlie", 21, 95]
# ]
# with open("students.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "age", "score"])
#     writer.writerows(rows)

# try:
#     with open("missing.txt", "r") as file:
#         data = file.read()
# except FileNotFoundError:
#     print("File not found")

# from pathlib import Path
# path = Path("../python/file.txt")
# with path.open("r", encoding="utf-8") as file:
#     for line in file:
#         text = line.strip()
#         if text:
#             print(text)

# with open("file.txt", "r", encoding="utf-8") as file:
#     print(file.tell())
#     file.read(5)
#     print(file.tell())

# with open("file.txt", "r", encoding="utf-8") as file:
#     print(file.read(5))
#     file.seek(0)
#     print(file.read(5))

with open("image.jpg", "rb") as file:
    data = file.read()

with open("image_copy.jpg", "wb") as file:
    file.write(data)

# Text files
# ↓
# "r"
# "w"
# "a"

# Binary files
# ↓
# "rb"
# "wb"
# "ab"