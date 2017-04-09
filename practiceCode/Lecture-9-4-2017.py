#print numbers which are divisble by 7 and 13
# for num in range(1,100):
#     if num%7==0 and num%13==0:
#         print(num)

# sentence = "The brown fox jumps quickly over the lazy dog"
# words = sentence.lower().split(' ')
# count = {}
# for w in words:
#     if w in count:
#         count[w] += 1
#     else:
#         count[w] = 1
# print(count)

# str = "Hello World"
# print(str[::-1])
# print(str[::2])
# count =0
# for alphabet in str:
#     if alphabet == 'a' or alphabet == 'i'or alphabet == 'e' or alphabet == 'o' or alphabet == 'u':
#         count =count+1
# print("Ther are %s vowels in string:"%count)


# def greet():
#     print("Hello World")
# greet()
#
# def greet_user(x):
#     print("Hello " + x)
#
# name = input("name????")
# greet_user(name)

# def add(num1,num2,num3):
#     print(num1+num2+num3)
# add(2,6,2)


# Note : List pass by reference , whereas digits and decimals pass by value

# e.g pass by value
# def abc(x):
#     x=90
# x=30
# abc(x)
# print(x)
#

# e.g pass by reference
# def abc(x):
#     x[0]=50
# x=[30,40,60,70]
# abc(x) #pass original list
# abc(x[:]) # pass copy of list
# print(x)


# def test(x,y=2):
#     print(x,y)
#
# test(5,4)
# test(x=1,y=5)
# test(y=5,x=1)
# test(x=6)
# test(6)

# def test(x,y):
#     return x+y
#
# result = test(3,4)
# print(result)
# print(test(3,4))

# def info(firstname,lastname):
#     return {"first_name":firstname,"last_name":lastname}
#
# print(info("Parkash","Kumar"))

# * is used to make tuple
# ** is used to make dictionary

# def demo(*nums):
#     return nums
# print(max(demo(10,20,40,15,24,25,80,100,89,120)))
# print(sum(demo(10,20,40,15,24,25,80,100,89,120))/len(demo(10,20,40,15,24,25,80,100,89,120)))


# def demodict(**dict):
#     return dict
# list1=[1,2,3]
# list2 =[3,14,5]
# result = demodict(list_one=list1,list_two=list2)
# newlist=[]
#
# for key,value in result.items():
#     newlist.append(value)
# print(newlist)