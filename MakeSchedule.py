import random
NumTeams = 16
TotalGames = 54
l = [x+1 for x in range(0,NumTeams)]

ScheduleTemplate = (1,2,3)
GamePath = '/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/schedules/'
GamePerWeek = ScheduleTemplate.__len__()
NumberOfGames = int(TotalGames / GamePerWeek)
TotalGamesPerTeam = NumberOfGames * GamePerWeek

GameTimes = {
    1: ['1805'],
    2: ['1135', '1205', '1405', '1645', '1905'],
    3: ['1205','1305','1805'],
    5: ['1805']
}

print('All Teams:',l)

def round_robin(teams, games):
    random.shuffle(teams)
    FullSchedule = []
    last = teams[-1]
    shape = teams[:-1]
    for g in range(games):
        ThisWeek = []
        mid = int(teams.__len__() / 2 - 1)
        for u in range(int((shape.__len__() - 1) / 2)):
            ThisWeek.append((shape[u], shape[-1*u - 1]))

        lasthomeflag = random.randint(0,1)
        if lasthomeflag == True:
            ThisWeek.append((shape[mid], last))
        else:
            ThisWeek.append((last, shape[mid]))
        shape.insert(0,shape.pop())
        FullSchedule.append(ThisWeek)

    return FullSchedule

r = round_robin(l, NumberOfGames)
week = 0
s = '<?xml version="1.0" encoding="ISO-8859-1"?>\n<SCHEDULE type="ILN_BGY_G' + str(TotalGamesPerTeam) + '_T' + str(NumTeams) + '" inter_league=\"0\" balanced_games=\"1\" games_per_team=\"' + str(TotalGamesPerTeam) + '\" preferred_start_day=\"6\">\n\t<GAMES>'
for u in r:
    print(u)
    for m in u:
        for g in ScheduleTemplate:
            gameday = week * 7 + g
            s += '\n\t\t<GAME day="' + str(gameday) + '" time="' + random.choice(GameTimes[g]) + '" away="' + str(m[0]) + '" home="' + str(m[1]) + '" />'

    week+=1

s += '	\n\t</GAMES>\n</SCHEDULE>'

print(s)
f = open(GamePath+'ILN_BGY_G' + str(TotalGamesPerTeam) + '_T' + str(NumTeams) + '_c_Custom.lsdl', 'w')
f.write(s)