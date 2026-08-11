# name: str = "Abhishek"
# age: int = 25
# is_adult: bool = True
# is_active: bool = False
# print(type(name))
# print(type(age))
# print(type(is_adult))
# print(type(is_active))

# def add(a: int, b: int) -> int:
#     return a + b
# print(add(10, 20))
# print(add("10", "20"))

# name: str | None = None
# print(type(name))
# name = "Abhishek"
# print(type(name))

# def calculate(value:int | float) -> float:
#     return value * 2
# print(calculate(10))
# print(calculate(10.5))

# from typing import TypeVar
# T = TypeVar("T")
# def add(a: T, b: T) -> T:
#     return a + b
# print(add(10, 20))
# print(add("10", "20"))

# from typing import TypedDict
# class User(TypedDict):
#     name: str
#     age: int
# user1: User = {
#     "name": "Abhishek",
#     "age": 25
# }
# user2: User = {
#     "name": "Abhishek",
#     "age": 25
# }
# print(user1)
# print(user2)

# from typing import Protocol
# class Predictor(Protocol):
#     def predict(self, input: str) -> str:
#         print("Predicting...")
#         return "Prediction"
# predictor = Predictor()
# print(predictor.predict("Hello"))

