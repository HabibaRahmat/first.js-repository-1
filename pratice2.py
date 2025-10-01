# def my_function(fname):
#   print(fname + " Smith")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Smith")
# my_function("yashhh", "karan")
# def my_function(*kids):
  #print(type(kids))
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias" )   
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Smith")
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
# my_function("mango")
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# def my_function(x, /):
#   print(x)
# my_function(3)
# my_function(4)
# my_function(6)
# def my_function(*, x):
#   print(x)

# my_function(x = 3)
# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
# my_function(5, 6, c = 7, d = 8)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# # print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# del thislist
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)
# def myfunc(n):
#   return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
