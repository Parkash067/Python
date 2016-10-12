#Step#1
# carDetails = {"name":"Civic","model":2016,"color":"Black"}
# print (carDetails)
# print (carDetails["name"])
# print (carDetails.keys())
# print (carDetails.values())
# print (carDetails.items())


#Step#2
# personInfo = {"Name":"Parkash Kumar","age":25,"city":"Karachi"}
# print (personInfo["Name"]+"\n"+str(personInfo["age"])+"\n"+personInfo["city"]);
#
# glossary = {"and":"It is a logical operation to satisfy two or more conditions at a time","lower()":"It is used to convert string in lowercase"}
# print (glossary["and"]+"\n"+glossary["lower()"])


# Step#3
# personInfo = {"Name":"Parkash Kumar","age":"25","city":"Karachi"}
# for key,value in personInfo.items():
#     print (key +":"+value)
#
# rivers = {"Nile": "Egypt", "Indus": "Pakistan", "Ganga": "India"}
# for key ,value in rivers.items():
#     print ("The "+key+" runs through "+value)
#
# print ("*#"*20)
#
# for name in rivers.keys():
#     print (name)
#
# print ("*#"*20)
#
# for country in rivers.values():
#     print (country)


# Step#4
# people_list = ["Ali","Maria","Farooq"]
# selected_people = {"Ali": "Python", "Parkash": "Typescript", "Zain": "Html"}
# print (selected_people.keys())
# for people in people_list:
#     if people in selected_people.keys():
#         print (people+" you are already enroll in a course")
#     else:
#         print (people+" you should take any course")

# Step#5
# customerInfo = {
#     "userOne": {
#         "firstName": "Parkash",
#         "lastName": "Kumar",
#         "age": 24,
#         "location": "pib colony",
#         "contact": [4648166, 4310038]
#     },
#     "userTwo": {
#         "firstName": "Zain",
#         "lastName": "Ansari",
#         "age": 30,
#         "location": "Gulshan",
#         "contact": [2648100, 4810038]
#     },
#     "userThree": {
#         "firstName": "Hadi",
#         "lastName": "Saeed",
#         "age": 41,
#         "location": "Defence",
#         "contact": [8648122, 2516638]
#     },
# }
#
# for key,value in customerInfo.items():
#     print ("Details of "+key+"\n"+value["firstName"]+"\n"+value["lastName"]+"\n"+str(value["age"])+"\n"+value["location"]+"\n"+str(value["contact"])+"\n")

#Step#6
# list_Dic = [
#     {"name":"parkash","sex":"male"},
#     {"name":"reeta","sex":"female"}
# ]
#
# for list in list_Dic:
#     print (list["name"]+" "+list["sex"])