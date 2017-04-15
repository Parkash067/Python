data = [2, 45, 4.5, 100, 144.3, 33.0, 30.67]
discrete = []
continuous = []
for number in data:
    if number % 1 == 0:
        discrete.append(number)
    else:
        continuous.append(number)

print ("Discrete Data :"+str(discrete))
print ("Continous Data : "+str(continuous))