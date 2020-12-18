# easy way
MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

newList = [x ** 2 for x in MyList]

myTuple = [(1, 2), (2, 3), (3, 4)]

newTuple = [x ** y for (y, x) in myTuple]

print(newList)
print(newTuple)

# old way

for (x, y) in myTuple:
    newTuple.append(x ** y)

print(newTuple)

# filtering data
newFilter = [x**y for(x, y) in myTuple if y < 5]
print(newFilter)


