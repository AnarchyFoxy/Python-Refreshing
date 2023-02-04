# 4.1 Pizza
pizzas = ["quatro formaggi", "double bacon burger", "pepperoni", "margarita"]
for pizza in pizzas:
    print(f"I like to eat {pizza} pizza. It is one of my favourite tastes")

print("I do really love pizza, I could eat it every single day")

# Output:
"""
I like to eat quatro formaggi pizza. It is one of my favourite tastes
I like to eat double bacon burger pizza. It is one of my favourite tastes
I like to eat pepperoni pizza. It is one of my favourite tastes
I like to eat margarita pizza. It is one of my favourite tastes
I do really love pizza, I could eat it every single day
"""

# 4.2 Animals
animals = ["fox", "cat", "wolf"]
for animal in animals:
    print(f"{animal.title()} is really cute. I wish to have one.")

print("All these animals are wonderful.")

# Output:
"""
Fox is really cute. I wish to have one.
Cat is really cute. I wish to have one.
Wolf is really cute. I wish to have one.
All these animals are wonderful.
"""

# 4.3 Counting to twelve
for i in range (1, 21):
    print(i)

# Output:
"""
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
"""

# 4.4. Milion
milion = [i for i in range(1, 1_000_001)]
print(milion)
print()

# Output:
# Well, it is to big to display here. Sorry.

# 4.5 milion summation
milion = [x for x in range(1, 1_000_001)]
print(min(milion))
print(max(milion))
print(sum(milion))

# Output:
"""
1
1000000
500000500000
"""

# 4.6 Odd lists
odds = [x for x in range(1, 20, 2)]
for odd in odds:
    print(odd)
print()

# Output:
"""
1
3
5
7
9
11
13
15
17
19
"""

# 4.7 Three
cubes = [x ** 3 for x in range(3, 30)]
for cube in cubes:
    print(cube)
print()

#Output:
"""
27
64
125
216
343
512
729
1000
1331
1728
2197
2744
3375
4096
4913
5832
6859
8000
9261
10648
12167
13824
15625
17576
19683
21952
24389
"""

# 4.8 & 4.9 cube with list comprehension
cubes = [x ** 3 for x in range(1, 11)]
for cube in cubes:
    print(cube)

# Output:
"""
1
8
27
64
125
216
343
512
729
1000
"""