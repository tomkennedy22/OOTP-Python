import random
Divisions = [0,1]
NumTeams = 134
Interleague = 'N'
BalancedGames = 'Y'
l = [x+1 for x in range(0,NumTeams)]
AllStarDay = 100
SplitSeason = True

#ScheduleTemplate = (1,2,3)

ScheduleTemplate = [
(1, [1,2,3]),
(1, [5]),
(2, [1,2,3]),
(2, [5]),
(3, [1,2,3]),
(3, [5]),
(4, [1,2,3]),
(4, [5]),
(5, [1,2,3]),
(5, [5]),
(6, [1,2,3]),
(6, [5]),
(7, [1,2,3]),
(8, [1,2,3]),
(9, [1,2,3]),
(10, [1,2,3]),
(11, [1,2,3]),
(12, [1,2,3]),
(13, [1,2,3]),
(14, [1,2,3]),
(15, [1,2,3]),
(16, [1,2,3])

]



GamePath = '/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/schedules/'

Rounds = ScheduleTemplate.__len__()
GamesPerTeam = sum([x[1].__len__() for x in ScheduleTemplate])
print(GamesPerTeam)

GameTimes = {
    1: ['1805'], #Friday
    2: ['1135', '1205', '1405', '1645', '1905'], #Saturday
    3: ['1205','1305','1805'], #Sunday
    4: ['1805'], #Monday
    5: ['1805'], #Tuesday
    6: ['1805', '1905'], #Wednesday
    7: ['1805', '1905'] #Thursday
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



week = 0
#_SL1_D1_T4_SL2_D1_T4
s = '<?xml version="1.0" encoding="ISO-8859-1"?>\n<SCHEDULE type="IL'+Interleague+'_BGY_G' + str(GamesPerTeam) + '_T' +str(NumTeams)+'" inter_league=\"0\" balanced_games=\"1\" games_per_team=\"' + str(GamesPerTeam) + '\"  allstar_game_day="'+ str(AllStarDay) +'" preferred_start_day=\"6\">\n\t<GAMES>'
for u in round_robin(l, len(ScheduleTemplate)):
    print('u',u)
    WeekHold = ScheduleTemplate[week]
    for m in u:
        print(m)
        teamGame = list(m)
        for g in WeekHold[1]:
            print(week, WeekHold[0], WeekHold[1], g)
            gameday = (WeekHold[0] - 1) * 7 + abs(g)
            print(teamGame)
            if g < 0:
                teamGame[0], teamGame[1] = teamGame[1], teamGame[0]
            s += '\n\t\t<GAME day="' + str(gameday) + '" time="' + random.choice(GameTimes[abs(g)]) + '" away="' + str(teamGame[0]) + '" home="' + str(teamGame[1]) + '" />'

    week+=1

s += '	\n\t</GAMES>\n</SCHEDULE>'

print(s)
f = open(GamePath+'IL'+Interleague+'_BGY_G' + str(GamesPerTeam) + '_T'+str(NumTeams)+'_c_NCAAT134G54_a.lsdl', 'w')
f.write(s)