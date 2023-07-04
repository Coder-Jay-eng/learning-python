def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num())
# prints out the largestnumber of the 3


def same_num(num1, num2):
    if num1 == num2:
        print("Numbers are similar")
    else:
        print("numbers not similar")


print(same_num())
