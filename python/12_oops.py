# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
# student = Student("Alice", 20)
# student.display()

# class BankAccount:
#     def __init__(self, balance): 
#         self.savings_interest_rate = 0.04
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}. \nNew balance: {self.balance}")
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}. \nNew balance: {self.balance}")
#         else:
#             print("Insufficient balance.")
#     @classmethod
#     def change_interest_rate(cls, new_rate):
#         cls.savings_interest_rate = new_rate
#         print(f"Interest rate changed to: {cls.savings_interest_rate}")
#     @staticmethod
#     def calculate_return(amount, duration):
#         return amount * (1 + BankAccount.savings_interest_rate) ** duration
# account = BankAccount(0)
# account.change_interest_rate(0.05)
# while True:
#     print("\nBank Account Menu:")
#     print("0. Check Interest Rate")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Calculate Return")
#     print("4. Exit")
#     choice = input("Enter your choice (0/1/2/3/4): ")
#     if choice == '0':
#         print(f"Current interest rate: {account.savings_interest_rate}")
#     elif choice == '1':
#         amount = float(input("Enter amount to deposit: "))
#         account.deposit(amount)
#     elif choice == '2':
#         amount = float(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
#     elif choice == '3':
#         amount = float(input("Enter amount to calculate return for: "))
#         duration = int(input("Enter duration in years: "))
#         return_value = account.calculate_return(amount, duration)
#         print(f"Calculated return: {return_value}")
#     elif choice == '4':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method.")
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  # Output: "Woof!"
# print(cat.speak())  # Output: "Meow!"

# class Animal:
#     def __init__(self, name):
#         self.name = name
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# class Animal:
#     def sound(self):
#         print("Some sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Dog:
#     def sound(self):
#         print("Bark")
# class Cat:
#     def sound(self):
#         print("Meow")

