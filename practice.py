print("Hello World")
print("Triangle Picture")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("Variables")
character_name = "John"
character_age = "35"
print("There once was a man named " +character_name+",")
print("he was " +character_age+" years old.")

character_name = "Mike"
print("He really liked the name " +character_name+",")
print("but didn't like being " +character_age+".")

print("Strings\nPeace World")
print("Peace\World")

phrase = "Peace World"
print(phrase + " is cool")

phrase = "The Academy"
print(phrase[0])
print(len(phrase))
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.index("T"))

print("Numbers in Python")
print(-3.0897)
print(2+8)
print(3*(4+5))
print(10 % 3)
my_num = 5
print(str(my_num) + " my fav number")
print(pow(5,2))

print("Getting Input From Users")

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name +" You are "+age)

print("Calculator in Python")
num1 = input("Enter a number: ")
num2 = input ("Enter another number: ")
result = int(num1) + int(num2)
print(result)

print("Lists")
friends = ["Dwight", "Jared", "Alvin"]
print(friends[-2])

print("List Functions")

lucky_numbers = [4,8,15,16,23,42]
friends = ["Dwight", "Jared", "Alvin"]
friends.extend(lucky_numbers)
friends.remove("Jared")
print(friends)

print("Tuples")
coordinates = [4,5]
coordinates[1] = 11
print(coordinates[1])

coordinates = [(4,5),(6,7),(80,34)]
print(coordinates[1])

print("Functions")
def say_hi(name, age):
   print("Hello " + name + ", you are " + age)
say_hi("Eric", "20")
# def is the key word in the function and indent and then call the function

print("Return Statement")
#getting information back from the code
#what happened in the code of data return information
def cube(num):
   return num*num*num  #give a number
print(cube(3))

def cube(num):
   return num*num*num  #give a number
result = cube(4)
print(result)

print("If Statements")
is_male = False
if is_male:
   print("You are a male")
else:
   print("You are not a male")
#OR
is_male = True
is_tall = True
if is_male or is_tall:
   print("You are a male or tall or both")
else:
   print("You are not a male or tall")
#AND
is_male = True
is_tall = True
if is_male and is_tall:
   print("You are a male or tall or both")
else:
   print("You are not a male or tall")

print("If Statements and Comparisons")
def max_num(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
       return num1
   elif num2 >= num1 and num2 >= num3:
       return num2
   else:
       return num3
print(max_num(3, 4, 5))

print("Dictionaries")
monthConversion = {
   "Jan" : "January",
   "Feb" : "Feburary",
   "Mar" : "March",
}
print(monthConversion.get("Feb"))

print("While Loop")
for letter in "The Grid" :
   print(letter)

friends = ["Dwight", "Jared", "Alvin"]
for friend in friends :
   print(friend)

friends = ["Dwight", "Jared", "Alvin"]
for index in range(3, 8) :
   print(index)

friends = ["Dwight", "Jared", "Alvin"]
for index in range(len(friends)):
   print(friends)

print("Exponent Function")

print("My Own Loops")
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for key, value in dt.items():
   print(key, value)

print("Arrays")
arr = [1,2,3,4,5,6,7]
arr.insert(3,10)
print(arr)

arr = [1,2,3,4,5,6,7]
arr.insert(7,11)
print(arr)

import array as arr
num_list = [2,5,62,5,42,52,48,5]
num_array = arr.array('i', num_list)
print(num_array[2:5])