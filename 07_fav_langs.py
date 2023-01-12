#using rstrip() and lstrip() functions

favourite_language = "Python "
print(favourite_language)

#temporary solution
print(favourite_language.rstrip())

print(favourite_language)

# permanent solution
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language2 = " Python "
print(favourite_language2.rstrip())
print(favourite_language2.lstrip())
print(favourite_language2.strip())

# Output:
"""
Python 
Python
Python 
Python
 Python
Python 
Python
"""