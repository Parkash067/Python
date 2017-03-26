"""
Python practice code - step by step
Book : Python Crash Course
"""

"""
Step#1
message = "Hello! This is my first Python program"
print(message)
"""

"""
Step#2
message = "Hello! This is my first Python program"
print(message)
message = "I feel comfortable in Python"
print (message)
"""

"""
Step#3
person_name = "parkash"
print("Helo "+person_name+" would you like to learn some Python today......")
"""

"""
Step#4
name = "Parkash"
print ("In upperCase: "+name.upper())
print ("In lowerCase: "+name.lower())
print ("In titleCase: "+name.title())
"""


"""
Step#5
famous_person = "parkash kumar"
print (famous_person.title()+" once said,'Excellence is never an accident.'")
"""


"""
Step#6
name = " Parkash Kumar "
print (name)
print ("lstrip: "+name.lstrip())
print ("rstrip: "+name.rstrip())
print ("strip: "+name.strip())
"""


"""
Step#7
print (5+3)
print (16-8)
print (16/2)
print (4*2)
"""



#Step#8
# fav_number = 7
# print("Hey your favourite number is: %s"%fav_number)
# print("Hey your favourite number is:"+str(fav_number))




#Step#10
#It prints The Zen of Python when you run a program
# import this


"""
Step#11
friends_list = ["Hadi","Zain","Mehreen"]
print (friends_list[0])
print (friends_list[1])
print (friends_list[2])
"""

"""
Step#12
friends_list = ["Hadi","Zain","Mehreen"]
print ("Hi .... " + friends_list[0])
print ("Hi .... " + friends_list[1])
print ("Hi .... " + friends_list[2])
"""


#Step#13
# tech_list = ["Python","Nodejs","Javascript"]
# print ("I want to learn these three languages:\t\n%s\t\n%s\t\n%s"%(tech_list[0],tech_list[1],tech_list[2]))



#Step#14
# guest_list = ["Hadi","Zain","Mehreen"]
# print ("Can make it")
# print (guest_list[0]+" please come tomorrow we will eat dinner together")
# print (guest_list[1]+" please come tomorrow we will eat dinner together")
# print (guest_list[2]+" please come tomorrow we will eat dinner together")
# cant_make_it = guest_list.pop(1)
# print (cant_make_it+" can't make it")
# guest_list.append("Aagha")
# guest_list.insert(0,"Maria")
# guest_list.insert(2,"Farooq")
# print ("New list",guest_list)
# del guest_list[0]
# print ("After del ",guest_list)
# guest_list.remove("Hadi")
# print ("After remove ",guest_list)


"""
Step#15
guest_list = ["Hadi","Zain","Mehreen"]
print ("Can make it")
print (guest_list[0]+" please come tomorrow we will eat dinner together")
print (guest_list[1]+" please come tomorrow we will eat dinner together")
print (guest_list[2]+" please come tomorrow we will eat dinner together")
cant_make_it = guest_list.pop(1)
print (cant_make_it+" can't make it")
guest_list.append("Aagha")
guest_list.insert(0,"Maria")
guest_list.insert(2,"Farooq")
print ("New list",guest_list)
del guest_list[0]
print ("After del ",guest_list)
guest_list.remove("Hadi");
print ("After remove ",guest_list)
"""


#Step#16
# places_list = ['Karachi','Lahore','Islamabad','Allahabad']
# print ("Original List ",places_list)
# print ("Sorted function ",sorted(places_list))
# print ("Sorted function with reverse order ",sorted(places_list,reverse=True))
# print ("Original List ",places_list)
# print ("Sorted function with reverse list ",sorted(places_list))
# places_list.sort()
# print ("Sort function ",places_list)
# places_list.sort(reverse=True)
# print ("Sort function with reverse",places_list)
# print ("Original List ",places_list)
# places_list.reverse()
# print ("Use reverse function ",places_list)
# places_list.reverse()
# print ("Use reverse function ",places_list)



"""
Step#17
dishes_list = ['Biryani','Pao Bhajee','Pani Puri']
for dish in dishes_list:
    print ("I like "+dish)
print ("These all dishes are my favourite I really like to eat all these dishes")
"""

"""
Step#18
animals_list = ['Horse','Dog','Cat']
for animal in animals_list:
    print ("A %s would make a great pet"%animal)
print ("These all animals are very faithful")
"""


"""
Step#19
for couting in range(1,21):
    print (couting)
"""

"""
Step#20
million_list = list(range(1,1000000))
for value in million_list:
    print (value)
"""

"""
Step#21
million_list = list(range(1,1000000))
print ("Max number: ",max(million_list))
print ("Min number: ",min(million_list))
print ("Sum: ",sum(million_list))
"""

"""
Step#22
number_list = list(range(1,20,2))
print ("Generate Odd numbers")
for number in number_list:
    print (number)
"""

"""
Step#23
multiples_list = list(range(3,31,3))
print ("Generate multiples of 3")
for number in multiples_list:
    print (number)
"""

"""
Step#24
cubes = []
numbers = list(range(1,11))
for value in numbers:
    cubes.append(value**3)
print ("Cubes: ",cubes)
"""


#Step#25
# cubes = [value**3 for value in range(1,11)]
# print (cubes)


#Step#26
# number_list=list(range(1,21))
# print("First three numbers in list: ",number_list[0:3])
# print("Last three numbers in list: ",number_list[-3:])



# Step#27
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between
# tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets
# tuple_list = (1,2,3)
# print ("Original Tuple list: ",tuple_list)
# tuple_list()
# # tuple_list[0]=5
# tuple_list = (4,5,6)
# print ("Modified Tuple list: ",tuple_list)


# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
#
# # Following action is not valid for tuples
# # tup1[0] = 100;
#
# # So let's create a new tuple as follows
# tup3 = tup1 + tup2
# print(tup3)
# print(sum(tup1))
#
# demotup = ('Hi...')*4
# print(demotup)


"""
Step#28
animals_list = ['Horse','Dog','Cat']
check = "Horse"
print (check not in animals_list);
"""

"""
Step#29
alien_color = "green"
if alien_color == "Red":
    print ("You have earned 15 points")
elif alien_color == "Yellow":
    print ("You have earned 10 points")
else:
    print ("You have earned 5 points")
"""


## STEP: MOre about variables and Printing
# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print ("Let's talk about %s." % my_name)
# print ("He's %d inches tall." % my_height)
# print ("He's %d pounds heavy." % my_weight)
# print ("Actually that's not too heavy.")
# print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
# print ("His teeth are usually %s depending on the coffee." % my_teeth)
#
# # this line is tricky, try to get it exactly right
# print ("If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight))

#Discuss in class lecture number two 26/3/2017
# names = ['a','b','c']
# for value in range(0,len(names)):
#    print(names[value])

#step#2
# squares = []
# for value in range(1,11):
#     squares.append(value**(1/2))
# print(squares)

# number = [1,2,3,4,5]
# increment = [value+1 for value in number]
# print(increment)

# for value in range(1,1000):
#     if value%15 == 0:
#         print(value)

#step3:
# names = ['Parkash', 'Hadi', 'Mehreen', 'Ali']
# for name in names[:2]:
#     print(name)

#shelock copying
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# my_foods.append('burger')
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

#deep copying
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods
# print("My favorite foods are:")
# my_foods.append('burger')
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# class assignment
# names = ['ali','riaz','fahd','hadi','salman','pk','aslma']
# _len=int(len(names)-1)
# print(names[0:4])
# print(names[int((len(names)/2))])
# print(names[int((len(names)/2)):])
# print(names[-3:])

