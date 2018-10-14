



CityFile = open('uscitiesv1.5.csv', 'r')

#OutputCityFile = open('uscitiesv1.5.csv', 'w')

count = 0


#city,state_name,lat,lng, population , population_proper ,density
for line in CityFile:
    count +=1
    if count == 1:
        continue


    linesplit = line.strip().split(',')
    print(linesplit)

    city = linesplit[0]
    state = linesplit[1]
    lat = linesplit[2].strip()
    long = linesplit[3].strip()
    population = int(linesplit[4].strip())



