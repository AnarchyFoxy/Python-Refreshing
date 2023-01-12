#!/usr/bin/env python3

# 2.1 simple message stored in variable and printed
message = "This is quite easy task to perform"
print(message)

# 2.2 simple message with overwritten content of first message
text = "This is 1st message"
print(text)
text = "This is 2nd message"
print(text)

# 2.3 Personal greetings
name = "Astryda"
print(f"Hello, {name}! Would you like to learn Python?")

# 2.4 using height letters functions
first_name = "aStRyDa "
last_name = "mAlInOwSkA"
full_name = first_name.capitalize() + last_name.capitalize()
print(full_name.lower())
print(full_name.upper())
print(full_name)

# 2.5 Famous quotation
author_name = "fryderyk"
author_last_name = "nietzsche"
famous_quote = "\"Whoever fights monsters should see to it that in the process he does not become a monster. And if you gaze long enough into an abyss, the abyss will gaze back into you.\"."
print(f"{author_name.capitalize()} {author_last_name.capitalize()} once said: {famous_quote}")

# 2.6 Famoous quotation 2, but in variable
author_and_quote_together = author_name.capitalize() + " " + author_last_name.capitalize() + " once said: " + famous_quote
print(author_and_quote_together)

# 2.7 using lstrip(), rstrip(), and strip() functions
my_name = "  Astryda    "
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.strip())

# 2.8 Multiple operations with result equal 8
print(5 + 3)
print(int(16 / 2))
print(10 - 2)
print(2 * 4)

# 2.9 favourite number stored in variable, then message contains variable, then printing message
fav_number = 1024
comm = f"my favourite number is: {fav_number}".capitalize()
print(comm)

# 2.10 - use comments in two selected tasks. Done more than twice

# 2.11 import the Zen of Python
import this