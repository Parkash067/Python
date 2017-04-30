#step#1
# str = "How are you?"
# print("Hi %s my friend"%(str))

#step#2
# s = 'STRING'
# print 'Place another string with a mod and s: %s' %(s)

#step#3
# Floating Point Numbers
# Floating point numbers use the format %n1.n2f where the n1 is the total minimum number of digits the string should contain
# (these may be filled with whitespace if the entire number does not have this many digits.
# The n2 placeholder stands for how many numbers to show past the decimal point. Lets see some examples:

# print 'Floating point numbers: %1.2f' %(13.144)
# print 'Floating point numbers: %1.0f' %(13.144)
# print 'Floating point numbers: %1.5f' %(13.144)
# print 'Floating point numbers: %10.2f' %(13.144)
# print 'Floating point numbers: %25.2f' %(13.144)

#step#4
# Using the string .format() method
# The best way to format objects into your strings for print statements is using the format method. The syntax is:

#'String here {var1} then also {var2}'.format(var1='something1',var2='something2')

#Lets see some examples:

print ('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print ('One: {p}, Two: {p}, Three: {p}'.format(p='hi'))

# Several Objects:
print ('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))

str = 'helo'
print ('This method is used to print string using format {greetings}'.format(greetings=str))