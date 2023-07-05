for letter in "Giraffe Academy":
    print(letter)
# prints every letter separately in the loop.

friends = ["Jim", "Jay", "Brian", "Don"]
for name in friends:
    print(name)
# prints every object in the array separately

for number in range(7):
    print(number)
# prints numbers in the range 0-7, excluding 7.


for number in range(7, 25):
    print(number)
# prints numbers in the range 7-25, excluding 25.


friends = ["Jim", "Jay", "Brian", "Don"]
# len(friends) -> prints the length of friends array, i.e 4
for index in range(len(friends)):
    print(friends[index])
# prints every object in the array separately
