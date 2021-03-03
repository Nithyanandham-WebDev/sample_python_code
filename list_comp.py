
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#a=[2221,12414,14124,14124124,124124,1414,1414,1414,354325,3523]
#apend object to the end of the list.
# a.append("a")
# print(a)
# a.append("nithya")
#Remove all items from list.
#a.clear()
# print(a)
#Return a shallow copy of the list.
#b=a
#print(b)
  # Return number of occurrences of value
# print(a.count(2221))
#Extend list by appending elements from the iterable
list_1=[1,2,3,4,5,6]
list_2=["nithya","balaji","vigenh"]

# list_extend
'''list_2.append(list_1)
print(list_2)
list_2.extend(list_1)
print(list_2)'''
x=[56,18,27,36,40]
y=["a","b","c","d","b"]
x.append(y)
# print(y)
x.extend(y)
# print(x)
# y.append(x)
# print(y)
# y.extend(x)
# print(y)
# Return first index of value.
# print(y.count("b"))
 # Insert object before index.
# y.insert(2,"demo")
# print(y)
# print(y.index("d"))
# y.insert(4,"root")
# print(y)
# print(y)
# y.insert(y.index("root"),"dell")
# print(y)
'''pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.'''
# print(y)
# y.pop()
# print(y)
#  # remove(self, valxue, /)
#  # |      Remove first occurrence of value.
#  # |      
#  # |      Raises ValueError if the value is not pres

# y.remove("b")

# print(y)
# y.remove("b")
# print(y)
# y.remove(()"b")
print(y)
  # reverse(self, /)
 # |      Reverse *IN PLACE*.
 # |  
# y.reverse()
# print(y[::-1)y]
y.sort()
print(y)

# a=[*range(61,156,6)]
# print(a)
# a.reverse()
# print(a)
# print(a[::-1])

a=[12,13,34,45,56,67,45,67,77]
print(a)
a.reverse()
print(a)
print(a[4])


print(dir(a))