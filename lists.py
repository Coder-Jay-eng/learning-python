friends = ["Kevin", "Karen", 63, 782, True, False]

print(friends[3])
# prints 782

print(friends[-1])
# prints False

print(friends[1:])
# prints elements from index 1 to the end as an array

print(friends[1:3])
# prints elements from position 1 to 3


friends[1] = "Jay"
print(friends[1])
# prints updated element: Jay

numbers = [73, 836, 9973864, 8636373]
friends.extend(numbers)
print(friends)
# prints friends list together with the numbers list

friends.append("Creed")
print(friends)
# adds item at the end of the list

friends.insert(1, "Kelly")
print(friends)
# prints friends with Kelly inserted at position 1 of the list

friends.remove("Kevin")
print(friends)
# removes Kelly from the list

friends.clear()
print(friends)
# gets rid of all elements in the list

friends.pop()
print(friends)
# removes last element from a list

print(friends.index("Jay"))
# prints the index of item "Jay" in the list friends

print(friends.count("Jay"))
# returns the number of times Jay appears in the string

friends.sort()
print(friends)
# sorts the list into alphabetical order, numerals from smallest to largest. Accepts oe type of data type

numbers.reverse()
print(numbers)
# prints the reversed version of the list

friends2 = friends.copy()
print(friends2)
# copies friends list into friends2
