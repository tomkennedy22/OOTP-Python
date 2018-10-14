import random
import itertools
import math

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


def round_robin(t, numGames):
    teams = t + []
    s = []
    n = []
    #random.shuffle(teams)
    for u in range(0, numGames):
        n = []
        mid = teams.__len__() / 2
        # print(mid, teams[mid:], teams[:mid])

        if u % 2 == 1:
            #print(zip(teams[mid:], teams[:mid]))
            n = n + zip(teams[mid:], teams[:mid])
        else:
            #print(zip(teams[:mid], teams[mid:]))
            n = n + zip(teams[:mid], teams[mid:])
        teams.insert(mid, teams.pop())
        s.append(n)


    return s

def round_robin2(t, numGames):
    teams = list(t)
    s = []
    n = []
    #random.shuffle(teams)
    print('')
    print('audit', teams.__len__(), teams, numGames)
    mid = 0
    if teams.__len__()  == 2 or numGames == 0:
        s = [(teams[0], teams[1])]
        for u in s:
            print(u)
        return s
    for u in range(0, int(math.ceil(numGames/2.0))):
        n = []
        mid = teams.__len__() / 2
        # print(mid, teams[mid:], teams[:mid])

        if u % 2 == 1:
            #print(zip(teams[mid:], teams[:mid]))
            n = n + zip(teams[mid:], teams[:mid])
        else:
            #print(zip(teams[:mid], teams[mid:]))
            n = n + zip(teams[:mid], teams[mid:])
        teams.insert(mid, teams.pop())
        s.append(n)

    for u in s:
        print(u)
    #print(round_robin2(l[mid:], numGames/2), round_robin2(l[:mid], numGames/2))
    secondhalf  = round_robin2(teams[mid:], teams[mid:].__len__() - 1)
    firsthalf = round_robin2(teams[:mid], teams[:mid].__len__() - 1)
    print('first', firsthalf, 'Second', secondhalf, 'together',[firsthalf] + [secondhalf])
    n = [firsthalf] + [secondhalf]
    s.append(n)
    #s.append(zip(firsthalf, secondhalf))

    return s




for u in round_robin(l,11):
    print(u)



rr2 = round_robin2(l,l.__len__() - 1)
print('break')

for u in rr2:
    print(u)

