#1 print one by one 
fruits = ['apple', 'banana', 'orange', 'kiwi', 'peaches', 'coconut', 'strawberry', 'mango', 'grapes', 'watermelon']
for i in fruits: # (i) same as saying the name of list (fruits)
    print(i)
#2 Loop over the list print last 3 letters of each fruit in list
for phrase in fruits:
    print(phrase[-3:])   
#3 Add numbers to the end of a list (loops)
n = 0
fruits = ['apple', 'banana', 'orange', 'kiwi', 'peaches', 'coconut', 'strawberry', 'mango', 'grapes', 'watermelon']
for phrase in fruits:
    print(phrase, n)
    n = n + 1
#4
n = 0
import glob
import re # new learned input 
pictures = glob.glob("/Users/wilson006/Desktop/Flood Pictures/*.png")
for image in pictures:
    print(image, n)
    n = n + 1 # need in order to make numbers start in order 
#5 Convert glob into string 
question_4 = ' '.join([str(elem) for elem in pictures]) #elem--> find given element 
question_4 = re.sub("[()]","", question_4) #re.sub--> change patterns delete specefic phrases from list 
question_4 = re.sub("[()]","", question_4)
print(question_4)
#6
q_4 = question_4.split()
print(q_4)
#7
big = []
small = []
for i in q_4:
    if len(i) > 4:
        big.append(i)
    else:
        small.append(i)
    print('big', big)
    print('small', small)
#8
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
for i in lst:
    while i == 100:
        print(100, lst.index(100))
        break