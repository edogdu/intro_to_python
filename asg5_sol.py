'''
asg5.py

Name:
Student ID:

Subject: Lists

Write the following functions
'''

# f1: (10 pts) sum the numbers in the list, skipping strings if any.
# Hint: Use try/except to skip strings
def sum_numbers(list):
	total = 0.0
	for x in list:
		try:
			total += x
		except:
			continue
	return total

# test
# print(sum_numbers([4,1.7,'a','hello',2.3]))
# Output:
# 8.0

# f2: (10 pts) double the elements of a number list
def double(list):
	for i in range(len(list)):
		list[i] = list[i] * 2

# test
# l = [1,5,7,9]
# double(l)
# print(l)
# Output:
# [2, 10, 14, 18]

# f3: (10 pts) add list1 elements to list2's end if they are 'not in' in list2
def add(list1, list2):
	for x in list1:
		if x not in list2:
			list2.append(x)

# test
# l1 = ['a','b','c']
# l2 = ['a','c','d','e']
# add(l1, l2)
# print(l2)
# Output:
# ['a', 'c', 'd', 'e', 'b']


# f4: (10 pts) count even numbers in an integer number list
def count_even(list):
	cnt = 0
	for x in list:
		if x%2 == 0:
			cnt += 1
	return cnt

# test
# print(count_even([1,2,5,8,9,12,14]))
# Output:
# 4

# f5: (10 pts) return a list of unique words from a given text
def words(text):
	# lower, split words to list
	list = text.lower().split()
	# sort the list
	list.sort()
	# create a new list with unique words ('append' if 'not in')
	newlist = []
	for w in list:
		if w not in newlist:
			newlist.append(w)
	# return the new list
	return newlist

# test
# print(words('One Fish Two Fish Red Fish Blue Fish'))
# Output:
# ['blue', 'fish', 'one', 'red', 'two']

# f6: (10 pts) return the longest string in a list of strings
def longest(list):
	longest = ''
	for w in list:
		if len(w) > len(longest):
			longest = w
	return longest

# test
# print(longest(['fish','one','longest','two','a']))
# Output:
# longest

# f7: (10 pts) return the size of the longest list in a list of lists
def longlistsize(list):
	longest = 0
	for l in list:
		if len(l) > longest:
			longest = len(l)
	return longest

# test
# print(longlistsize([[1,2,3],[3,5],[5,6,7,8],[1]]))
# Output:
# 4

# f8: (10 pts) return a list of numbers from 0 to num
def numberlist(num):
	return [x for x in range(num)]

# test
# print(numberlist(7))
# Output:
# [0, 1, 2, 3, 4, 5, 6]

# f9: (10 pts) flatten a list of lists
# Hint: use list comprehension with nested for
def flatten(list):
	return [y for x in list for y in x ]

# test
# print(flatten([[1,2,3],[3,5],[5,6,7,8],[1]]))
# Output:
# [1, 2, 3, 3, 5, 5, 6, 7, 8, 1]

# f10: (10 pts) return the sizes of strings in a list
# Hint: list comprehension!
def sizes(list):
	return [len(s) for s in list]

# test
# print(sizes(['fish','one','longest','two','a']))
# Output:
# [4, 3, 7, 3, 1]