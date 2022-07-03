#1
print('Welcome to The Bank of Cash')
pin=int(input("Enter your pin number please: "))
print(pin)
if (pin == 1252):
    print("Welcome, how much money do you want to withdraw?")
else:
    print("Sorry, you have entered a wrong pin, please try again.")

#2
num = int(input("Pick a Number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

#3
num_2 =int(input("Pick Another Number: "))
if num_2 % 4 == 0:
    print("Hello")
else:
    print("Bye")

#4
grade = int(input("Enter Grade: "))
if grade >90:
    print("A")
elif grade >80 and grade <=90:
    print("B")
elif grade >=60 and grade <=80:
    print("C")
elif grade <=60:
    print("D")
else:
    print("fail")


#5
print("Enter the Year: ")
y = int(input())

if y%4==0 and y%100!=0:
    print("\nIt is a Leap Year")
elif y%400==0:
    print("\nIt is a Leap Year")
else:
    print("\nIt is not a Leap Year")

#6
people = ["Mark", "Bj", "Christian", "Zuri"]
if "person" in people: #Chage name to configure if' esle statement 
    print("Name is present.")
else:
    print("Name not found")