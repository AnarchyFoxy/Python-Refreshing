#!/usr/bin/env python3

# 3.1 friends names in array
names = ["Astryda", "Ingeborga", "Adrian", "Inez"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print()

# 3.2 Personalised greetings with names contained in array from first task
print(f"Hello, {names[0]}! How are you?")
print(f"Hello, {names[1]}! My dearest, I hope you are feeling well.")
print(f"Hello, {names[2]}! You are such a lovely boy.")
print(f"Hello, {names[3]}! I hope you will find your love.")
print()

# 3.3 My own array
dreams = ["Mazda MX-5", "horror book", 100000]
print(f"I wish to have {dreams[0]}, as I do really like this car.")
print(f"I wish to publish my own {dreams[1]}, as I'm writing it sinse 2011.")
print(f"I wish to earn {dreams[2]} every month to perform all necessary medical operations.")
print()

# 3.4 Party array
guests = ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum"]
print(f"Hello, {guests[0]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[1]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[2]}! I would like to invite you to my pizza party!")
print()

# 3.5 Changing guest array
print(f"Unfortunately, {guests[0]} can't arrive on our party :c")
print("I have to modify our guest list :c")
guests[0] = "Steve Jobs"
print(f"Hello, {guests[0]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[1]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[2]}! I would like to invite you to my pizza party!")
print()

# 3.6 Expanding array
print("Good news, fellows! I have found bigger table for our pizza party!")
guests.insert(0, "Fryderyk Nietzsche")
guests.insert(2, "Ada Lovelace")
guests.append("Murray Rothbard")
print(f"Hello, {guests[0]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[1]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[2]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[3]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[4]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[5]}! I would like to invite you to my pizza party!")
print()

# 3.7 Reducing array size
print("Oh no!!! The promised bigger table will not be delivered on time!")
print("I can invite only two of you, guys...")
popped_guest = guests.pop()
print(f"I'm so sorry, {popped_guest}, we will meet again next time :c")
popped_guest = guests.pop()
print(f"I'm so sorry, {popped_guest}, we will meet again next time :c")
popped_guest = guests.pop()
print(f"I'm so sorry, {popped_guest}, we will meet again next time :c")
popped_guest = guests.pop()
print(f"I'm so sorry, {popped_guest}, we will meet again next time :c")
print("So, let's check who is finally invited: ")
print(f"Hello, {guests[0]}! I would like to invite you to my pizza party!")
print(f"Hello, {guests[1]}! I would like to invite you to my pizza party!")
print("Ok, now I can clean all guests array")
del guests[1]
del guests[0]
print(guests)
print()

# 3.8 Jumping all over the world
cities = ["Thesaloniki", "Athina", "Helsinki", "Espoo", "Oslo"]
print("Original array:")
print(cities)
print("\nnow temporary reversed")
print(sorted(cities))
print("\nNow again initial order")
print(cities)
print("\nNow temporary reversed")
print(sorted(cities, reverse=True))
print("\nSee? original array is intact")
print(cities)
print("\nSo, time for reverse:")
cities.reverse()
print(cities)
print("\nNow time for restore")
cities.reverse()
print(cities)
print("\nLet's permanent sort")
cities.sort()
print(cities)
print("\nReversed sort")
cities.sort(reverse=True)
print(cities)
print()

# 3.9 Counting guests
print("So, I've invited", len(guests), "guests")
print()

# 3.10 using all functions together
task_list = ["Thesaloniki", "Athina", "Helsinki", "Espoo", "Oslo", "Makedonija", "Lublana"]
print(task_list)
task_list.append("Moskwa")
print(task_list)
task_list.insert(5, "Sandevistan")
print(task_list)
del task_list[-1]
print(task_list)
popped_out = task_list.pop()
print(task_list, popped_out)
task_list.remove("Makedonija")
print(task_list)
print(sorted(task_list))
print(task_list)
task_list.reverse()
print(task_list)
task_list.sort()
print(task_list)
print(len(task_list))

#append(), insert(), del, pop(), remove(), sort(), sorted(), reverse(), len()

# Output:
"""
Astryda
Ingeborga
Adrian
Inez

Hello, Astryda! How are you?
Hello, Ingeborga! My dearest, I hope you are feeling well.
Hello, Adrian! You are such a lovely boy.
Hello, Inez! I hope you will find your love.

I wish to have Mazda MX-5, as I do really like this car.
I wish to publish my own horror book, as I'm writing it sinse 2011.
I wish to earn 100000 every month to perform all necessary medical operations.

Hello, Dennis Ritchie! I would like to invite you to my pizza party!
Hello, Bjarne Stroustrup! I would like to invite you to my pizza party!
Hello, Guido van Rossum! I would like to invite you to my pizza party!

Unfortunately, Dennis Ritchie can't arrive on our party :c
I have to modify our guest list :c
Hello, Steve Jobs! I would like to invite you to my pizza party!
Hello, Bjarne Stroustrup! I would like to invite you to my pizza party!
Hello, Guido van Rossum! I would like to invite you to my pizza party!

Good news, fellows! I have found bigger table for our pizza party!
Hello, Fryderyk Nietzsche! I would like to invite you to my pizza party!
Hello, Steve Jobs! I would like to invite you to my pizza party!
Hello, Ada Lovelace! I would like to invite you to my pizza party!
Hello, Bjarne Stroustrup! I would like to invite you to my pizza party!
Hello, Guido van Rossum! I would like to invite you to my pizza party!
Hello, Murray Rothbard! I would like to invite you to my pizza party!

Oh no!!! The promised bigger table will not be delivered on time!
I can invite only two of you, guys...
I'm so sorry, Murray Rothbard, we will meet again next time :c
I'm so sorry, Guido van Rossum, we will meet again next time :c
I'm so sorry, Bjarne Stroustrup, we will meet again next time :c
I'm so sorry, Ada Lovelace, we will meet again next time :c
So, let's check who is finally invited: 
Hello, Fryderyk Nietzsche! I would like to invite you to my pizza party!
Hello, Steve Jobs! I would like to invite you to my pizza party!
Ok, now I can clean all guests array
[]

Original array:
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo']

now temporary reversed
['Athina', 'Espoo', 'Helsinki', 'Oslo', 'Thesaloniki']

Now again initial order
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo']

Now temporary reversed
['Thesaloniki', 'Oslo', 'Helsinki', 'Espoo', 'Athina']

See? original array is intact
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo']

So, time for reverse:
['Oslo', 'Espoo', 'Helsinki', 'Athina', 'Thesaloniki']

Now time for restore
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo']

Let's permanent sort
['Athina', 'Espoo', 'Helsinki', 'Oslo', 'Thesaloniki']

Reversed sort
['Thesaloniki', 'Oslo', 'Helsinki', 'Espoo', 'Athina']

So, I've invited 6 guests

['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Makedonija', 'Lublana']
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Makedonija', 'Lublana', 'Moskwa']
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Sandevistan', 'Makedonija', 'Lublana', 'Moskwa']
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Sandevistan', 'Makedonija', 'Lublana']
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Sandevistan', 'Makedonija'] Lublana
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Sandevistan']
['Athina', 'Espoo', 'Helsinki', 'Oslo', 'Sandevistan', 'Thesaloniki']
['Thesaloniki', 'Athina', 'Helsinki', 'Espoo', 'Oslo', 'Sandevistan']
['Sandevistan', 'Oslo', 'Espoo', 'Helsinki', 'Athina', 'Thesaloniki']
['Athina', 'Espoo', 'Helsinki', 'Oslo', 'Sandevistan', 'Thesaloniki']
6
"""