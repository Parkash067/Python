import random
# with open('./files/demo.txt') as file_object:
#     contents = file_object.read()
#     data = contents.split(' ')
#     for i in data:
#         print(i)

    # read line by line
    # for line in file_object:
    #     print(line)

# with open('./files/demo.txt','w') as file_object:
#     file_object.write('I love Programming')

# try:
#     with open('./files/abc.txt') as file_object:
#         contents = file_object.read()
# except:
#     print("File is not present in current directory")
#
# else:
#     print("print successfully")
#
# finally:
#     print("Its done")

# rand = [(random.random())*10+10 for _ in range(0,5)]
# for num in rand:
#     print('{i}'.format(i=num))


count = 0
def passingStd(stu):
    if stu == "Pass":
        count = count + 1
    return count

def result(student):
    if student > 40:
        return "Pass"
    else:
        return "Fail"

students = [85,97,40]

check = map(result,students)
filter_ = filter(passingStd,check)

print(check)
print (filter_)
# for i, student in enumerate(students):
#     check = result(i,student)
#     print check