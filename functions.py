intro = 'Hello World! This is my first "python program". '

# converts to lower or upper case.
print(intro.lower() + "I am super excited.".upper())
# prints hello world! this is my first "python program". I AM SUPER EXCITED.

# checks if string is lower or upper case.
print(intro.islower())
# prints False

print(intro.lower().islower())
# prints True

print(len(intro))
# prints number of characters in string

print(intro[0])
# prints first character

print(intro[7])
# prints character at the position passed


print(intro.index("i"))
# prints the position in which the character first appears in the string

print(intro.index("This"))
# prints the position in which the word starts

print(intro.replace("first", "tenth"))
# replaces the word first with the word tenth
