# 5.1 conditional tests
car = "subaru"
print("Does car == \"subaru\"? I predict True value")
print(car == "subaru")

print("\nDoes car == \"audi\"? I predict False value")
print(car == "audi")

# Output:
"""
Does car == "subaru"? I predict True value
True

Does car == "audi"? I predict False value
False
"""

# 5.2 More conditional tests
print("Does  \"mazda\" == \"audi\"? I predict False.")
print("mazda" == "audi")

print("\nDoes \"Mazda\".lower() == \"mazda\"? I predict True")
print("Mazda".lower() == "mazda")

print()
print(5 > 4)
print(5 < 4)
print(13 >= 10)
print(13 <= 10)

print(5 > 4 and 5 > 6)
print(5 > 4 or 5 > 10)

print()
print("Let's check cars!")
cars = ["mazda", "audi", "bmw", "subaru"]
print("mazda" in cars)

bannerlords = ["gazela", "kicia", "ferdek"]
user = "asta"
if user not in bannerlords:
    print(f"Hello, {user.title()}")

# Output:
"""
Does  "mazda" == "audi"? I predict False.
False

Does "Mazda".lower() == "mazda"? I predict True
True

True
False
True
False
False
True

Let's check cars!
True
Hello, Asta
"""