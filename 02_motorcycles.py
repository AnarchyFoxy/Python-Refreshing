# Using arrays method - append(), insert(), del, pop(), remove()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)
print()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print()

motorcycles = []
print(motorcycles)
motorcycles.append("honda")
motorcycles.append("suzuki")
motorcycles.append("yamaha")
print(motorcycles)
print()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
print()

# Removing elements from array
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
print()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
last_owned = motorcycles.pop()
print(f"My last motorcycle was {last_owned.title()}")
print(motorcycles)
print()

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"My first motorycycle I've bought was: {first_owned.title()}")
print(motorcycles)
print()

motorcycles = ["honda", "ducati", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)
print()

motorcycles = ["honda", "ducati", "yamaha", "suzuki"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nThe {too_expensive.title()} motorcycle was too expensive for me")
print()


# Output:
"""
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']

[]
['honda', 'suzuki', 'yamaha']

['honda', 'yamaha', 'suzuki']
['ducati', 'honda', 'yamaha', 'suzuki']

['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki

['honda', 'yamaha', 'suzuki']
My last motorcycle was Suzuki

['honda', 'yamaha', 'suzuki']
My first motorycycle I've bought was: Honda
['yamaha', 'suzuki']

['honda', 'ducati', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki']

['honda', 'ducati', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki']

The Ducati motorcycle was too expensive for me
"""