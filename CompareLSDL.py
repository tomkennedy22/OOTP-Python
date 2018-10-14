OOTPFile = open('/Users/tom/OOTP Staging/testtesttest.lsdl', 'r')
PythonFile = open('/Users/tom/OOTP Staging/ILN_BGY_G54_T134_c_NCAA_a.lsdl', 'r')

OOTPTeams = {}
PythonTeams = {}

for l in OOTPFile:
    s = l.strip().split(' ')
    #print(s)
    if '<GAME ' in l:
        #print('game in here')
        hello = 0
    else:
        continue

    for attr in s:
        if '"' in attr:
            if 'day=' in attr:
                Day = int(attr.split('"')[1])
            elif 'time=' in attr:
                Time = int(attr.split('"')[1])
            elif 'away=' in attr:
                Away = int(attr.split('"')[1])
            elif 'home=' in attr:
                Home = int(attr.split('"')[1])

    #print(Day, Time, Home, Away)
    if Home in OOTPTeams:
        OOTPTeams[Home].append('Home on day ' + str(Day) + ' at ' + str(Time))
    else:
        OOTPTeams[Home] = []
        OOTPTeams[Home].append('Home on day ' + str(Day) + ' at ' + str(Time))

    if Away in OOTPTeams:
        OOTPTeams[Away].append('Away on day ' + str(Day) + ' at ' + str(Time))
    else:
        OOTPTeams[Away] = []
        OOTPTeams[Away].append('Away on day ' + str(Day) + ' at ' + str(Time))


for l in PythonFile:
    s = l.strip().split(' ')
    #print(s)
    if '<GAME ' in l:
        #print('game in here')
        hello = 0
    else:
        continue

    for attr in s:
        if '"' in attr:
            if 'day=' in attr:
                Day = int(attr.split('"')[1])
            elif 'time=' in attr:
                Time = int(attr.split('"')[1])
            elif 'away=' in attr:
                Away = int(attr.split('"')[1])
            elif 'home=' in attr:
                Home = int(attr.split('"')[1])

    #print(Day, Time, Home, Away)
    if Home in PythonTeams:
        PythonTeams[Home].append('Home on day ' + str(Day) + ' at ' + str(Time))
    else:
        PythonTeams[Home] = []
        PythonTeams[Home].append('Home on day ' + str(Day) + ' at ' + str(Time))

    if Away in PythonTeams:
        PythonTeams[Away].append('Away on day ' + str(Day) + ' at ' + str(Time))
    else:
        PythonTeams[Away] = []
        PythonTeams[Away].append('Away on day ' + str(Day) + ' at ' + str(Time))

s = ''
for t in OOTPTeams:
    #print(t)
    #print(OOTPTeams[t])

    for p in PythonTeams:
        if OOTPTeams[t] == PythonTeams[p]:
            #print(t,p, OOTPTeams[t], PythonTeams[p])
            s += str(t) + ',' + str(p) + '\n'

print(s)

f = open('PythonToOOTPTeamCompare.txt', 'w')
f.write(s)


