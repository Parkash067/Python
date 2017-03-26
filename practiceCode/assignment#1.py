#TASK#1
# number = int(input("Enter Number? "))
# reverse = 0
# while number > 0:
#     reverse = reverse*10 + number%10
#     number = number /10
# print reverse

#TASK#2
# months = ['January','February','March','April','May','June','July','August','September','October','November','Decemeber']
# days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# number = int(input('Enter number of month in interger? '))
# print "Name of month is %s "%months[number-1]
# print "Number of days in this months:%d"%days_in_month[number-1]

#TASK#3
# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# number = int(input('Enter number of day in interger? '))
# print "Name of day is %s"%days[number-1]

#Task#4
# radius = float(input('Enter number of day in interger? '))
# print "Area of sphere is %f "%((1.33)*(3.142)*(radius*radius*radius))

#Task#5
# height = float(input('Enter number height of a traingle? '))
# base = float(input('Enter number base of a traingle? '))
# print "Area of a triangle is %f "%(base*height/2)

#Task#6
# coefficient_x_sq = int(input('Enter coefficient of x square: '))
# coefficient_x = int(input('Enter coefficient of x: '))
# constant_term = int(input('Enter constant term: '))
# positive_root = -(coefficient_x + ((coefficient_x**2) - (4*coefficient_x_sq*constant_term))**0.5)/(2*coefficient_x_sq)
# negaive_root = -(coefficient_x - ((coefficient_x**2) - (4*coefficient_x_sq*constant_term))**0.5)/(2*coefficient_x_sq)
# print "The roots of quadratic equation are %f and %f"%(positive_root,negaive_root)