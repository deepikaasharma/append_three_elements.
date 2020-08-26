"""Write a function called append_three_elements. This function takes four arguments as parameters. The first is a list, called lst, that you will be appending to. The next three parameters will be objects that need to be added to the list, a, b, and c, respectively. This function should return a new list with the three values appended in order at the end. See example:

append_three_elements([], 1, 2, 3)

you would expect to return

[1, 2, 3] """

lst =[]
a = 'a'
b = 'b'
c = 'c'
def append_three_elements(lst,a,b,c):
  lst.append(a)
  lst.append(b)
  lst.append(c)
  return lst

print(append_three_elements(lst,a,b,c))

