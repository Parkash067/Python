# Step#1  Basic Calculator
# import mathsFun as _maths
# active = True
# while active:
#     number1 = raw_input("Enter first number: ")
#     number2 = raw_input("Enter second number: ")
#     operation = raw_input("Apply operations + / * - on numbers")
#     if operation == "+":
#         add = _maths.add(int(number1),int(number2))
#         print ("Result is %s"%add)
#     elif operation == "-":
#         diff = _maths.diff(int(number1),int(number2))
#         print ("Result is %s"%diff)
#     elif operation == "*":
#         prod = _maths.prod(int(number1),int(number2))
#         print ("Result is %s" % prod)
#     elif operation == "/":
#         div = _maths.divide(int(number1), int(number2))
#         print ("Result is %s" % div)
#     else:
#         active = False
#         print ("You entered invalid operation on number")

#Step#2
# def make_shirt(size, message):
#     print (message + size +" size")
#
# make_shirt("medium","I want to buy this tshirt but in ")#postional arguments
# make_shirt(message="I want to buy this tshirt but in ",size="medium")# keyword arguments

#step#3
# def make_shirt(size, message="I love python"):
#     print (size +"\n"+message)
#
# make_shirt(size="medium")
# make_shirt(size="small",message="I love nodejs")

#Step#4
# def city_country(city, country):
#     return {"city":city,"country":country}
# result=city_country("Karachi","Pakistan")
# print ("'"+result["city"]+"'"+", "+"'"+result["country"]+"'")
# result=city_country("Delhi","India")
# print ("'"+result["city"]+"'"+", "+"'"+result["country"]+"'")

#step#5
# def album_info(album, artist):
#     return {"album":album,"artist":artist}
#
# active = True
# while active:
#     album = raw_input("Enter name of album: ")
#     artist = raw_input("Enter name of artist: ")
#     show = raw_input("Do you want to show the album info? y or n")
#     if show == 'y':
#         result = album_info(album,artist)
#         print ("This album '%s' is created by %s"%(result["album"], result["artist"]))
#     else:
#         active = False
#         print ("You are not in interested in album info")


#Step#6
# magicianList = ["Zakoota", "Dajal", "Najoomi"]
# def magician(magicianList):
#     for magicain in magicianList:
#         print (magicain)
#
# magician(magicianList)