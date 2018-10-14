import glob
import operator
import random
import math
import itertools


###############################
# WORLD CONFIG HERE

ConferencePrestiges = {
    'SEC': 18,
    'ACC': 15,
    'Big 12': 14,
    'Pac 12': 14,
    'Big 10': 8,
    'Ivy League': 3,
    'AAC': 7,
    'C-USA': 5,
    'Big West': 9,
    'Sun Belt': 6,
    'Mountain West': 5,
    'Big East': 3
}

TeamPrestiges = {
    'Miami': 18,
    'Virginia': 15,
    'Florida State': 14,
    'North Carolina': 14,
    'Boston College': 3,
    'Florida': 16,
    'Arizona State': 15,
    'Georgia': 15,
    'LSU': 15,
    'Mississippi State': 15,
    'Ole Miss': 15,
    'Oregon State': 15,
    'Vanderbilt': 14,
    'Arizona': 13,
    'Georgia Tech': 13,
    'Kentucky': 13,
    'Louisville': 13,
    'TCU': 13,
    'USC': 13,
    'Texas A&M': 13,
    'South Carolina': 12,
    'Texas': 12,
    'Alabama': 11,
    'Arkansas': 11,
    'Stanford': 10,
    'Texas Tech': 10,
    'UCLA': 10,
    'Oklahoma State': 9,
    'Rice': 9,
    'Auburn': 8,
    'Baylor': 8,
    'NC State': 8,
    'Missouri': 8,
    'California': 7,
    'Oklahoma': 7,
    'Tennessee': 7,
    'Virginia Tech': 7,
    'West Virginia': 7,
    'Duke': 6,
    'Syracuse': 6,
    'Iowa State': 5,
    'Kansas': 5,
    'Kansas State': 5,
    'Oregon': 5,
    'SMU': 5,
    'Washington': 5,
    'Colorado': 4,
    'Utah': 4,
    'Washington State': 4,
    'Wake Forest': 3,
    'Harvard': 2,
    'Brown': 1,
    'Columbia': 1,
    'Cornell': 1,
    'Dartmouth': 1,
    'Penn': 1,
    'Princeton': 1,
    'Yale': 1,
    'Ohio State': 6,
    'Michigan': 6,
    'Michigan State': 6,
    'Penn State': 6,
    'Illinois': 7,
    'Indiana': 5,
    'Wisconsin': 4,
    'Rutgers': 6,
    'USF': 4,
    'Iowa': 4,
    'Colorado State': 3,
    'North Carolina State': 6,
    'Fresno State': 4,
    'San Diego State': 7,
    'Clemson': 12,
    'Southern Mississippi': 7,
    'North Texas': 3,
    'Pittsburgh': 2,
    'Nebraska': 3,
    'Old Dominion': 1,
    'Northwestern': 3,
    'UAB': 3,
    'Georgia Southern': 3,
    'FIU': 2,
    'New Mexico': 1,
    'Marshall': 1,
    'Boise State' : 3,
    'Air Force' : 2,
    'UNLV' : 5,
    'BYU' : 2,
    'San Jose State' : 4,
    'Nevada' : 4,
    'Texas-Arlington' : 3,
    'Arkansas State' : 3,
    'Louisiana-Monroe' : 4,
    'Troy' : 3,
    'Texas State' : 2,
    'Arkansas-Little Rock' : 3,
    'Coastal Carolina' : 6,
    'Appalachian State' : 4,
    'Louisiana-Lafayette' : 3,
    'South Alabama' : 3,
    'Georgia State' : 4,
    'Cal State Fullerton' : 8,
    'UC Riverside' : 4,
    'UC Santa Barbara' : 5,
    'Pepperdine' : 2,
    'San Diego' : 4,
    'Hawaii' : 1,
    'UC Irvine' : 3,
    'Cal Poly' : 6,
    'Long Beach State' : 8,
    'Gonzaga' : 2,
    'UC Davis' : 2,
    'Cal State Northridge' : 2,
    'UNC Greensboro' : 2,
    'North Carolina-Charlotte' : 2,
    'Florida Atlantic' : 4,
    'Texas-San Antonio' : 3,
    'Louisiana Tech' : 5,
    'Western Kentucky' : 2,
    'Middle Tennessee' : 2,
    'Florida International' : 2,
    'Wichita State' : 4,
    'Army' : 0,
    'UCF' : 6,
    'Temple' : 3,
    'Navy' : 0,
    'East Carolina' : 1,
    'Connecticut' : 2,
    'Memphis' : 4,
    'Tulane' : 4,
    'Houston' : 5,
    'Cincinnati' : 3,
    'Purdue' : 4,
    'Maryland' : 5,
    'Minnesota' : 2,
    'Tulsa': 2,
    'Fordham': 1,
    'Lehigh': 1,
    'Villanova': 2,
    'Georgetown': 2,
    'Lafayette': 1,
    "St. John's": 2,
    'Boston': 2,
    'Providence': 3,
    'Seton Hall': 1,
    'Colgate': 1
}

PositionValues = {
    1: 10,
    2: 7,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
    8: 0,
    9: -1,
    10: -2,
    11: -3,
    12: -4
}

ScheduleTemplate = [
(1, [1,2,3], 0),
(1, [5],0 ),
(2, [1,2,3], 0),
(2, [5], 0),
(3, [1,2,3], 0),
(3, [5], 0),
(4, [1,2,3], 0),
(4, [5], 0),
(5, [1,2,3], 0),
(5, [5], 0),
(6, [1,2,3], 0),
(6, [5], 0),
(7, [1,2,3], 1),
(8, [1,2,3], 1),
(9, [1,2,3], 1),
(10, [1,2,3], 1),
(11, [1,2,3], 1),
(12, [1,2,3], 1),
(13, [1,2,3], 1),
(14, [1,2,3], 1),
(15, [1,2,3], 1),
(16, [1,2,3], 1)
]


GameTimes = {
    1: ['1905', '2005'], #Friday
    2: ['1205', '1305', '1405', '1905', '2005'],#Saturday
    3: ['1305', '1405', '1905'],#Sunday
    4: ['1905'],#Monday
    5: ['1805', '1905'],#Tuesday
    6: ['1905'],#Wednesday
    7: ['1905'],#Thursday

}


#player_id	league_id	team_id	sub_league_id	award_id	year	season	position	day	month
#Award Notes
#ID 0 - Player of the Week
#ID 1 - Pitcher of the Month
#ID 2 - Batter of the Month
#ID 3 - Rookie of the month
#ID 4 - Pitcher of the Year
#ID 5 - MVP
#ID 6 - Rookie of the year
#ID 7 - Gold Glove
#ID 11 - Silver Slugger
#ID 13 - Reliver of the year


#coach_id	first_name	last_name	nick_name	age	date_of_birth	city_of_birth_id	nation_id	weight	height	position	experience	occupation	team_id	former_player_id	quick_left	contract_salary	contract_years	contract_extension_salary	contract_extension_years	scout_major	scout_minor	scout_international	scout_amateur	scout_amateur_preference	teach_hitting	teach_pitching	teach_fielding	handle_veterans	handle_rookies	handle_players	strategy_knowledge	heal_legs	heal_arms	heal_back	heal_other	heal_rest	management_style	personality	hitting_focus	pitching_focus	training_focus	teach_running	prevent_legs	prevent_arms	prevent_back	prevent_other	stealing	running	pinchrun	pinchhit_pos	pinchhit_pitch	hook_start	hook_relief	closer	lr_matchup	bunt_hit	bunt	hit_run	run_hit	squeeze	pitch_around	intentional_walk	hold_runner	guard_lines	infield_in	outfield_in	corners_in	shift_if	shift_of	num_pitchers	num_hitters	favor_speed_to_power	favor_avg_to_obp	favor_defense_to_offense	favor_pitching_to_hitting	favor_veterans_to_prospects	trade_aggressiveness	player_loyalty	trade_frequency	trade_preference	value_stats	value_this_year	value_last_year	value_two_years	draft_value	intl_fa_value	develop_value	ratings_value	manager_value	pitching_coach_value	hitting_coach_value	scout_value	doctor_value	busy	type	data	days_left
#Coach Notes
#ID 1 - Manager
#ID 2 - Bench Coach
#ID 4 - Pitching Coach
#ID 5 - Hitting Coach
#ID 7 - Scout
#ID 8 - Trainer

#COLUMNS:
#TeamID - 13
#teach_hitting	teach_pitching	teach_fielding 26,27,28
#handle_rookies	handle_players 30,31
#loyalty - 79
#coach valie - 90


###############################


###############################
#  GLOBAL VARIABLES HERE
PrestigeWeight = .25
CoachWeight = .2
TeamPerformance1YearWeight = .3
TeamPerformance4YearWeight = .2
TeamPerformance8YearWeight = .15
TeamPerformance18YearWeight = .05
PlayerAwardWeight = .05
ConferenceWeight = .2

HeaderRowCount = 0
PrestigeBaseline = 1
CoachBaseline = 1
TeamPerformance1YearBaseline = 1
TeamPerformance4YearBaseline = 1
TeamPerformance8YearBaseline = 1
TeamPerformance18YearBaseline = 1
PlayerAwardBaseline = 1
ConferenceBaseline = 1

LeagueName = 'NCAA'
LeagueID = 100

TopTierSize = 1
TierGrowthRate = .5

DraftRounds = 10

NumberOfGames = 0

for u in ScheduleTemplate:
    NumberOfGames += u[1].__len__()

ManualSubsetSpacing = None

DivisionDict = {}
TeamDict = {}
CorrectTeamMap = {}

GamePath = '/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/saved_games/NCAA-1840.lg/'
SchedulePath  = '/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/schedules/'
DraftPath = GamePath + 'import_export/draft.csv'

DumpPath = GamePath + 'dump/*'
max = ''


#############################
#############################


#############################
# CLASS DEFINITIONS HERE
class League:
    Divisions = []
    LeagueName = ''
    LeagueID = 0

    def __init__(self, name, id):
        self.LeagueID = id
        self.LeagueName = name
        self.Divisions = []

    def add_division(self, div):
        self.Divisions.append(div)

    def count_number_teams(self):
        sum = 0
        for d in self.Divisions:
            t = d.Teams.__len__()
            sum += t
        return sum

    def __str__(self):
        writeStr = 'League name: ' + self.LeagueName + '.  '
        writeStr += 'This league has ' + str(self.Divisions.__len__()) + ' conferences'

        return writeStr


class Division:
    League = None
    Teams = []
    DivisionName = ''
    DivisionID = 0
    ConferencePrestige = 0
    Schedule = {}

    def __init__(self, name, id):
        self.Teams = []
        self.DivisionID = id
        self.DivisionName = name
        self.Schedule = {}
        self.ConferencePrestige = 0

    def add_team(self, team):
        self.Teams.append(team)

    def __str__(self):
        writeStr = 'Division name: ' + self.DivisionName + '.  '
        writeStr += 'This division has prestige of ' + str(self.ConferencePrestige) + '. '
        writeStr += 'This division has ' + str(self.Teams.__len__()) + ' teams'

        return writeStr

    def pop_schedule(self):
        u = round_robin([x.TeamName for x in self.Teams], 11)
        count = 0
        for x in u:
            self.Schedule[count] = x
            count +=1

class Coach:
    Team = None
    Name = ''
    CoachValue = 1
    TeachHitting = 0
    TeachPitching = 0
    TeachFielding = 0
    HandlePlayers = 0
    HandleRookies = 0
    PlayerLoyalty = 0
    CoachValue = 0


    def __init__(self, t, n, TH, TP, TF, HP, HR, PL, CV):
        self.Team = t
        self.Name = n
        self.TeachHitting = TH
        self.TeachPitching = TP
        self.TeachFielding = TF
        self.HandlePlayers = HP
        self.HandleRookies = HR
        self.PlayerLoyalty = PL
        self.CoachValue  = CV

    def calc_coach_value(self):

        Value = self.TeachFielding + self.TeachPitching + self.TeachHitting + self.HandleRookies + self.HandlePlayers + (30 * self.PlayerLoyalty) + self.CoachValue
        return Value

class Team:
    Divison = None
    TeamName = ''
    TeamNickName = ''
    TeamID = 0
    TeamPrestige = 0
    Tier = 0
    Rank = -1
    AdjustedTeamID = 0
    PlayoffWins = 0

    Years = {}
    Picks = []
    Games = []
    Coach = None

    def __init__(self, name, nickname, id, adj):
        self.TeamName = name
        self.TeamNickName = nickname
        self.TeamID = id
        self.Years = {}
        self.Picks = []
        self.Tier = 0
        self.Rank = -1
        self.TeamPrestige = 0
        self.AdjustedTeamID = adj
        self.PlayoffWins = 0
        self.Games = []
        self.Coach = None

    def add_year(self, ts):
        year = ts.Year
        self.Years[year] = ts

    def calc_team_performance(self, y):
        count = 0
        sum = 0
        if self.Years.__len__() == 0:
            return 0

        if y ==1:
            sum+=self.PlayoffWins

        for u in sorted(self.Years, reverse=True):
            count +=1
            if count > y:
                count -=1
                break
            sum += self.Years[u].calc_score()

        return sum * 1.0 / count

    def SetBaselines(self):
        global TeamPerformance1YearBaseline
        global TeamPerformance4YearBaseline
        global TeamPerformance8YearBaseline
        global TeamPerformance18YearBaseline
        global PrestigeBaseline
        global ConferenceBaseline
        global CoachBaseline

        TeamPerformance1YearBaseline = MaxOfTwoNumbers(int(TeamPerformance1YearBaseline) , self.calc_team_performance(1))
        TeamPerformance4YearBaseline = MaxOfTwoNumbers(int(TeamPerformance4YearBaseline), self.calc_team_performance(4))
        TeamPerformance8YearBaseline = MaxOfTwoNumbers(int(TeamPerformance8YearBaseline), self.calc_team_performance(8))
        TeamPerformance18YearBaseline = MaxOfTwoNumbers(TeamPerformance18YearBaseline, self.calc_team_performance(18))
        PrestigeBaseline = MaxOfTwoNumbers(PrestigeBaseline, self.TeamPrestige)
        ConferenceBaseline = MaxOfTwoNumbers(ConferenceBaseline, self.Divison.ConferencePrestige)
        CoachBaseline = MaxOfTwoNumbers(CoachBaseline, self.Coach.calc_coach_value())

    def calc_rating(self):
        global TeamPerformance1YearBaseline
        global TeamPerformance4YearBaseline
        global TeamPerformance8YearBaseline
        global TeamPerformance18YearBaseline
        global PrestigeBaseline
        global ConferenceBaseline
        global CoachBaseline

        TeamPerformance1Year = TeamPerformance1YearWeight * self.calc_team_performance(1)  / TeamPerformance1YearBaseline
        TeamPerformance4Year = TeamPerformance4YearWeight * self.calc_team_performance(4) / TeamPerformance4YearBaseline
        TeamPerformance8Year = TeamPerformance8YearWeight * self.calc_team_performance(8) / TeamPerformance8YearBaseline
        TeamPerformance18Year = TeamPerformance18YearWeight * self.calc_team_performance(18) / TeamPerformance18YearBaseline
        TeamPrestige = PrestigeWeight * self.TeamPrestige / PrestigeBaseline
        ConferencePrestige = ConferenceWeight * self.Divison.ConferencePrestige / ConferenceBaseline
        CoachPrestige = CoachWeight * self.Coach.calc_coach_value() / CoachBaseline

        sum = TeamPerformance1Year + TeamPerformance4Year + TeamPerformance8Year + TeamPerformance18Year + TeamPrestige + ConferencePrestige + CoachPrestige
        return sum


    def __str__(self):
        writeStr = 'Team name: ' + self.TeamName + ' ' + self.TeamNickName +'.  '
        writeStr += 'This team name changed IDs from ' + str(self.TeamID) + ' to ' + str(self.AdjustedTeamID) + '. '
        writeStr += 'This team has prestige of ' + str(self.TeamPrestige) + '. '
        writeStr += 'This team played baseball in the following seasons: ' + ', '.join([str(x) for x in self.Years]) + '.  '
        writeStr += 'This team is playing ' + str(len(self.Games)) + ' games this year, with ' + str(len([x for x in self.Games if x.HomeTeam == self.TeamID])) + ' at home'
        return writeStr

class TeamSeason:
    Year = 0
    Wins = 0
    GB = 0
    Team = None
    Position = 0
    MadePlayoffs = 0
    WonChampionship = 0

    def __init__(self, year, wins, gb, pos, team):
        self.Year = year
        self.Wins = wins
        self.GB = gb
        self.MadePlayoffs = 0
        self.WonChampionship = 0
        self.Team = team
        self.Position = pos

    def calc_score(self):
        sum = 0

        if self.Position in PositionValues:
            sum += PositionValues[self.Position]
        else:
            sum -= 5

        sum += self.MadePlayoffs * 5
        sum += self.WonChampionship * 10

        return sum

    def __str__(self):
        writeStr = 'Team name: ' + self.Team.TeamName + ' ' + self.Team.TeamNickName +'.  '
        writeStr += 'In the year ' + str(self.Year) + ' the team won ' + str(self.Wins) + ' games, finished in ' + str(self.Position) + ' spot, and scores ' + str(self.calc_score())
        return writeStr

class Draft:
    Rounds = {}

    def __init__(self):
        self.Rounds = {}

    def export_draft(self, f):
        writestring = ''
        for r in self.Rounds:
            for p in self.Rounds[r].Picks:
                f.write(p.pick_output())

    def __str__(self):
        return ''

class Round:
    Picks = []
    RoundNumber = 0

    def __init__(self, rn):
        self.Picks = []
        self.RoundNumber = rn

    def __str__(self):
        return ''

class Pick:
    Team = None
    Round = None
    PickNumber = -1

    def __init__(self, team, round, picknumber):
        self.Team = team
        self.Round = round
        self.PickNumber = picknumber


    def __str__(self):
        s = self.Team.TeamName + ' is picking in round ' + str(self.Round.RoundNumber)
        s += ' with pick ' + str(self.PickNumber)
        return s

    def pick_output(self):

        # //Format: Draft Round	 Supplemental (1 = yes or 0 = no)	 Pick in Round	 Team Name	 Team ID	 Player ID
        s = str(self.Round.RoundNumber) + ', 0, ' + str(self.PickNumber) + ', ' + self.Team.TeamName + ', ' + str(self.Team.TeamID) + ',0\n'
        return s


class Schedule:
    Weeks = []

    def __init__(self):
        self.Weeks = []

    def export_schedule(self,f):
        s = '<?xml version="1.0" encoding="ISO-8859-1"?>\n<SCHEDULE type="ILN_BGY_G'+ str(NumberOfGames) +'_T'+ str(LeagueObject.count_number_teams()) +'" inter_league=\"0\" balanced_games=\"1\" games_per_team=\"'+ str(NumberOfGames) +'\" preferred_start_day=\"6\">\n\t<GAMES>'

        for W in self.Weeks:
            for M in W.Matchups:
                for G in M.Games:
                    s+= '\n\t\t<GAME day="'+str(G.Day)+'" time="'+G.Time+'" away="'+str(TeamDict[M.AwayTeam].AdjustedTeamID)+'" home="'+str(TeamDict[M.HomeTeam].AdjustedTeamID)+'" />'

        s+='	\n\t</GAMES>\n</SCHEDULE>'
        f.write(s)

class Week:
    Matchups = []
    GameSchedule = []

    WeekNumber = -1
    ConferencePlay = None
    StartingDay = -1
    MidWeek = None

    NumberOfGames = -1

    def __init__(self, weeknum, day, midweek, conf,games):
        self.Matchups = []
        self.WeekNumber = weeknum
        self.ConferencePlay = conf
        self.StartingDay = day
        self.MidWeek = midweek
        self.GameSchedule = games

    def teams_playing_this_week(self):
        teamlist = []
        for m in self.Matchups:
            for g in m.Games:
                teamlist.append(g.HomeTeam.TeamID)
                teamlist.append(g.AwayTeam.TeamID)

        teamlist = list(set(teamlist))
        return teamlist

    def make_matchups(self, s, w):
        for m in s:
            if (random.choice([True, False]) == True):

                M = Matchup(m[0], m[1])
            else:
                M = Matchup(m[1], m[0])
            self.Matchups.append(M)

            for game in self.GameSchedule:
                day = self.StartingDay  + game
                time = random.choice(GameTimes[game])
                rg = M.add_game(day, time)
                TeamDict[m[0]].Games.append(rg)
                TeamDict[m[1]].Games.append(rg)


class Matchup:

    NumberOfGames = 0
    HomeTeam = None
    AwayTeam = None
    Week = None
    Games = []

    def __init__(self, h,a):

        self.HomeTeam = h
        self.AwayTeam = a
        self.Games = []


    def add_game(self, d, t):
        G = Game(self.HomeTeam, self.AwayTeam, d, t)
        self.Games.append(G)
        return G


class Game:

    Day = -1
    Time = ''

    def __init__(self, h, a, d, t):
        self.HomeTeam = h
        self.AwayTeam = a
        self.Day = d
        self.Time = t

    def __str__(self):

        s = ''

        s+= TeamDict[self.AwayTeam].TeamName + ' at ' + TeamDict[self.HomeTeam].TeamName + ' on day '+ str(self.Day)
        return s

###########################
###########################


###########################
# PROCEDURE DEFINITIONS HERE

def make_tiers(pop, tier1, tiergrowth):
    size = tier1
    count = 0
    tiercutoffs = []
    while count < pop:
        count += size
        size += tiergrowth
        tiercutoffs.append(count)
    return tiercutoffs


def round_robin(teams, games):
    random.shuffle(teams)
    FullSchedule = []
    last = teams[-1]
    shape = teams[:-1]
    for g in range(games):
        ThisWeek = []
        mid = int(teams.__len__() / 2 - 1)
        for u in range(int((shape.__len__() - 1) / 2)):
            if random.choice([True, False]) == True:
                ThisWeek.append((shape[u], shape[-1*u - 1]))
            else:
                ThisWeek.append((shape[-1 * u - 1], shape[u]))

        if random.choice([True, False]) == True:
            ThisWeek.append((shape[mid], last))
        else:
            ThisWeek.append((last, shape[mid]))
        shape.insert(0,shape.pop())
        FullSchedule.append(ThisWeek)

    return FullSchedule

def MaxOfTwoNumbers (a,b):
    if a > b:
        return a
    else:
        return b

###########################

CorrectTeamMapFile = open('PythonToOOTPTeamCompare.txt', 'r')

for l in CorrectTeamMapFile:
    CSVSplit = l.strip().split(',')
    Orig = int(CSVSplit[0])
    Adj = int(CSVSplit[1])
    #print(Orig,Adj)
    CorrectTeamMap[Orig] = Orig

for folder in glob.glob(DumpPath):
    if folder > max:
        max = folder

SubFolder = max + '/csv/'
NoneCoach = Coach(0,'',0,0,0,0,0,0,0)
LeagueFile = open(SubFolder + 'leagues.csv', 'r')

count = 0
for l in LeagueFile:
    count += 1
    if count == HeaderRowCount:
        continue
    #print(l)
    CSVSplit = l.replace('"', '').split(',')
    #print(CSVSplit)
    ParsedLeagueID = CSVSplit[0]
    ParsedLeagueName = CSVSplit[1]

    if LeagueName == ParsedLeagueName:
        LeagueID = int(ParsedLeagueID)

print(LeagueName, LeagueID)
LeagueObject = League(LeagueName, int(LeagueID))

DivisionFile = open(SubFolder + 'divisions.csv', 'r')

count = 0
for l in DivisionFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')
    print(CSVSplit)
    ParsedLeagueID = int(CSVSplit[0])
    ParsedDivisionID = int(CSVSplit[2])
    ParsedDivisionName = CSVSplit[3]

    if ParsedLeagueID == LeagueID:
        d = Division(ParsedDivisionName, int(ParsedDivisionID))
        if ParsedDivisionName in ConferencePrestiges:
            d.ConferencePrestige = ConferencePrestiges[ParsedDivisionName]
        else:
            print(ParsedDivisionName, 'not in Conference Prestige Config!!')
        DivisionDict[ParsedDivisionID] = d
        LeagueObject.add_division(d)

TeamFile = open(SubFolder + 'teams.csv', 'r')
count = 0
for l in TeamFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')
    ParsedLeagueID = int(CSVSplit[7])
    ParsedDivisionID = int(CSVSplit[9])
    ParsedTeamID = int(CSVSplit[0])
    ParsedTeamName = CSVSplit[1]
    ParsedTeamNickName = CSVSplit[3]

    if ParsedLeagueID == LeagueID:
        t = Team(ParsedTeamName, ParsedTeamNickName, ParsedTeamID, CorrectTeamMap[ParsedTeamID])

        if ParsedTeamName in TeamPrestiges:
            t.TeamPrestige = TeamPrestiges[ParsedTeamName]
        else:
             print(ParsedTeamName, 'not in Team Prestige Config!!')

        t.Divison = DivisionDict[ParsedDivisionID]

        TeamDict[ParsedTeamID] = t
        DivisionDict[ParsedDivisionID].add_team(t)


#'teamdict', TeamDict)
TeamHistoryRecordFile = open(SubFolder + 'team_history_record.csv', 'r')
count = 0
for l in TeamHistoryRecordFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')
    ParsedLeagueID = int(CSVSplit[2])
    ParsedYear = int(CSVSplit[1])
    ParsedTeamID = int(CSVSplit[0])
    ParsedWins = int(CSVSplit[6])
    ParsedPosition = int(CSVSplit[8])
    ParsedGB = float(CSVSplit[10])


    if ParsedLeagueID == LeagueID:
        ts = TeamSeason(ParsedYear, ParsedWins, ParsedGB, ParsedPosition, TeamDict[ParsedTeamID])
        TeamDict[ParsedTeamID].add_year(ts)



#print('teamdict', TeamDict)
TeamHistoryFile = open(SubFolder + 'team_history.csv', 'r')
count = 0
for l in TeamHistoryFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')
    ParsedLeagueID = int(CSVSplit[2])
    ParsedYear = int(CSVSplit[1])
    ParsedTeamID = int(CSVSplit[0])
    ParsedMadePlayoffs = int(CSVSplit[12])
    ParsedWonChampionship = int(CSVSplit[13])


    if ParsedLeagueID == LeagueID:
        ts = TeamDict[ParsedTeamID].Years[ParsedYear]
        ts.MadePlayoffs = ParsedMadePlayoffs
        ts.WonChampionship = ParsedWonChampionship

#print('teamdict', TeamDict)
PlayoffFile = open(SubFolder + 'league_playoff_fixtures.csv', 'r')
count = 0
for l in PlayoffFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')
    ParsedLeagueID = int(CSVSplit[0])
    ParsedRound = int(CSVSplit[7])
    ParsedWinningTeamID = int(CSVSplit[3])

    if ParsedLeagueID == LeagueID:
        TeamDict[ParsedWinningTeamID].PlayoffWins += ParsedRound


#CoachFile = open(SubFolder + 'coaches.csv', 'r')

count = 0
for l in []:#CoachFile:
    count += 1
    if count == HeaderRowCount:
        continue
    CSVSplit = l.replace('"', '').split(',')


    ParsedTeamID = int(CSVSplit[13])
    ParsedTeachHitting = int(CSVSplit[25])
    ParsedTeachPitching = int(CSVSplit[26])
    ParsedTeachFielding = int(CSVSplit[27])
    ParsedHandlePlayers = int(CSVSplit[29])
    ParsedHandleRookies = int(CSVSplit[30])
    ParsedLoyalty = int(CSVSplit[78])
    ParsedValue = int(89)
    if ParsedTeamID == 0:
        continue

    C = Coach(ParsedTeamID, '', ParsedTeachHitting, ParsedTeachPitching, ParsedTeachFielding, ParsedHandlePlayers, ParsedHandleRookies, ParsedLoyalty, ParsedValue)
    TeamDict[ParsedTeamID].Coach = C


for u in TeamDict:
    if TeamDict[u].Coach is None:
        TeamDict[u].Coach = NoneCoach
    TeamDict[u].SetBaselines()

TeamsSortedByValue = sorted(TeamDict.items(), key=operator.itemgetter(1))
sortedTeams = sorted(TeamDict.items(), key=lambda x: x[1].calc_rating(), reverse=True)

count = 0
TierCutoffs = make_tiers(LeagueObject.count_number_teams(), TopTierSize, TierGrowthRate)
maxtier = 0
for u in sortedTeams:
    count+=1
    TeamDict[u[0]].Rank = count
    a = [x for x in TierCutoffs if x >= TeamDict[u[0]].Rank][0]
    TeamDict[u[0]].Tier = TierCutoffs.index(a) + 1

    if TierCutoffs.index(a) + 1 > maxtier:
        maxtier = TierCutoffs.index(a) + 1

    print(count, TeamDict[u[0]].TeamName, TeamDict[u[0]].TeamID, TeamDict[u[0]].calc_rating(), TeamDict[u[0]].Rank, TeamDict[u[0]].Tier)


DraftObject = Draft()

for u in range(1, maxtier+DraftRounds):
    R = Round(u)
    DraftObject.Rounds[u] = R

    TeamsThisRound = [x for x in TeamDict if (TeamDict[x].Tier <= u and TeamDict[x].Picks.__len__() < DraftRounds)]
    random.shuffle(TeamsThisRound)
    count = 1
    for team in TeamsThisRound:
        P = Pick(TeamDict[team], R, count)
        R.Picks.append(P)
        TeamDict[team].Picks.append(P)
        count+=1

WriteDraft = open(DraftPath, 'w')

DraftObject.export_draft(WriteDraft)


ScheduleObject = Schedule()

count = 0
for u in round_robin([TeamDict[t].TeamID for t in TeamDict], len([x for x in ScheduleTemplate if x[2] == 0])):#[x for x in ScheduleTemplate]:

    WeekNum = u[0]
    StartDay = 7 * ScheduleTemplate[count][0] - 7

    W = Week(WeekNum, StartDay, False, 0, ScheduleTemplate[count][1])

    ScheduleObject.Weeks.append(W)
    W.make_matchups(u, ScheduleTemplate[count])
    count +=1

prevcount = count
for d in DivisionDict:
    count = prevcount
    for u in round_robin([t.TeamID for t in DivisionDict[d].Teams], len([x for x in ScheduleTemplate if x[2] == 1])):#[x for x in ScheduleTemplate]:

        WeekNum = u[0]
        StartDay = 7 * ScheduleTemplate[count][0] - 7

        W = Week(WeekNum, StartDay, False, 0, ScheduleTemplate[count][1])

        ScheduleObject.Weeks.append(W)
        W.make_matchups(u, ScheduleTemplate[count])
        count +=1

WriteSchedule = open(SchedulePath+'ILN_BGY_G'+str(NumberOfGames)+'_T'+str(LeagueObject.count_number_teams())+'_c_NCAA_a.lsdl', 'w')

ScheduleObject.export_schedule(WriteSchedule)

#######################



#######################
# FINAL AUDIT
print(LeagueObject)
for d in LeagueObject.Divisions:
    print(d)
    for t in d.Teams:
        print(t)
        t.calc_rating()
        if t.TeamName not in TeamPrestiges:
            print('\''+t.TeamName+'\' : '+'XXX,')
#####################


print('Created schedule' + WriteSchedule.name)