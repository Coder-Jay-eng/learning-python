is_male = True

if is_male:
    print("You are a male")

# prints "You are a male."


is_male = False
if is_male:
    print("You are a male")

# doesn't print a thing/ blank


is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")

# prints "You are male if true", "You are not male if false"


is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
    # only one condition has to be true
else:
    print("You are neither a male nor tall")


is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
    # both the conditions have to be true
else:
    print("You are either not male or not tall or both")


is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
    # both the conditions have to be true
elif is_male and not (is_tall):  # else if statement
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are tall but not a male")
else:
    print("You are not a male and not tall")
