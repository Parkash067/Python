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


"""
Step#8
fav_number = 7
print ("Hey your favourite number is: %s"%fav_number)
"""


"""
Step#10
import this
It prints The Zen of Python when you run a program
"""

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

"""
Step#13
tech_list = ["Python","Nodejs","Javascript"]
print ("I want to learn these three languages:\t\n%s\t\n%s\t\n%s"%(tech_list[0],tech_list[1],tech_list[2]))
"""

"""
Step#14
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

"""
Step#16
places_list = ['Karachi','Lahore','Islamabad','Allahabad']
print ("Original List ",places_list)
print ("Sorted function ",sorted(places_list))
print ("Sorted function with reverse order ",sorted(places_list,reverse=True))
print ("Original List ",places_list)
print ("Sorted function with reverse list ",sorted(places_list))
places_list.sort()
print ("Sort function ",places_list)
places_list.sort(reverse=True)
print ("Sort function with reverse",places_list)
print ("Original List ",places_list)
places_list.reverse()
print ("Use reverse function ",places_list)
places_list.reverse()
print ("Use reverse function ",places_list)
"""


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

"""
Step#25
cubes = [value**3 for value in range(1,11)]
print (cubes)
"""

"""
Step#26
number_list=list(range(1,21))
print ("First three numbers in list: ",number_list[0:3])
print ("Last three numbers in list: ",number_list[-3:])
"""

"""
Step#27
tuple_list = (1,2,3)
print ("Original Tuple list: ",tuple_list)
#tuple_list[0]=5
tuple_list = (4,5,6)
print ("Modified Tuple list: ",tuple_list)
"""

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



