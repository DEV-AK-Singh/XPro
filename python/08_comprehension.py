## LIST COMPREHENSION
# squares = [i**2 for i in range(0, 10)]
# print(squares)

# collection = [1, 2, 3, 4, 5]
# new_collection = [i * 2 for i in collection]    
# print(new_collection)

# collection = [1, 2, 3, 4, 5]
# new_collection = [i * 2 for i in collection if i % 2 == 0]
# print(new_collection)

# names = ["Alice", "Bob", "Charlie"]
# uppercase = [name.upper() for name in names]
# print(uppercase)

# words = ["python", "ai", "machine learning"]
# lengths = [len(word) for word in words]
# print(lengths)

# numbers = [1, 2, 3, 4, 5]
# labels = ["ODD" if num % 2 !=0 else "EVEN" for num in numbers]  
# print(list(zip(numbers, labels)))

## SET COMPREHENSION
# numbers = {x ** 2 for x in range(5)}
# print(numbers)

# words = ["AI", "AI", "Python", "Python"]
# unique = {word for word in words}
# print(unique)

## DICTIONARY COMPREHENSION
# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 35, 40]
# people = {name: age for name, age in zip(names, ages)}
# print(people)

# EXAMPLE
# text = "Python AI Python Machine Learning AI"
# vocabulary = {
#     word.lower() for word in text.split()
# }
# print(vocabulary)

ages = [18, 21, 30, 45]
age_groups = {
    age: ( "Teen" if age < 20 else "Adult" ) for age in ages
}
print(age_groups)