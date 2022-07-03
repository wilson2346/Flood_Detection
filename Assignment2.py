#1
name = input("Enter Name: ")
print(name)
#2
first_name = "Eric"
last_name = "Wilson"
print(first_name[0:4])
print(last_name[0:6])
#3
print(first_name[::-1])
print(last_name[::-1])
#4
print("Pick a number")
value = int(input())
math = value / 2 
print("When you divide the number by two, you will get:" + str(math))
#5
sentence = "We have to eat, exercise, work, laugh, love, and be happy"
#6
no_space_string = sentence.replace(' ','')
print(no_space_string)
#7
print(sentence.split(','))
