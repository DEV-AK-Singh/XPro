# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# finally:
#     print("Execution completed.")

# try:
#     number = int(input("Number: "))
#     result = 100 / number
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print("Invalid input")

# try:
#     number = int(input("Number: "))
# except ValueError:
#     print("Invalid input: Please enter a valid integer.")
# else:
#     print("You entered:", number)

# try:
#     number = int(input("Enter number: "))
#     result = 100 / number
# except ValueError:
#     print("Invalid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Result:", result)
# finally:
#     print("Operation completed")

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
# except ValueError as e:
#     print("Error:", e)
# else:
#     print("Your age is:", age)
# finally:
#     print("Execution completed.")

# import json
# def load_config(path):
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Configuration file not found: {path}")
#     except json.JSONDecodeError as error:
#         raise ValueError("Configuration contains invalid JSON") from error
# try:
#     config = load_config("file1.csv")
#     print(config)
# except FileNotFoundError as e:
#     print(e)
# except ValueError as e:
#     print(e)