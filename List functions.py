
lucky_numbers = [5,15,16,18,20,]
friends = ["Tony", "Karen", "John", "John", "Reuben", "Jake"]

friends2 = friends.copy()

#sort the list in ascending order
friends.sort()
print(friends)

#adding 2 lists together
friends.extend(lucky_numbers)
print(friends)

#adding another name to the end of a list
friends.append("Creed")
print(friends)

#inserting a name in a designated spot in list
friends.insert(1, "Nathaniel")
print(friends)

#deleting a name from a list
friends.remove("Tony")
print(friends)

#pop an item off of the list
friends.pop(0)
print(friends)

#find certain value on list
print(friends.index("Nathaniel"))

#count how many times a value pops up
print(friends.count("John"))

#removing everything from a list
friends.clear()
print(friends)

#copying a list
print(friends2)


