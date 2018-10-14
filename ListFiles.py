import glob
import os

path = '/Users/tom/OOTP Staging/_NeedsHelp/*.png'
strippedpath = '/Users/tom/OOTP Staging/_NeedsHelp/'

LogoInfoFile = open('LogoInfoFile.csv', 'w')
LogoInfoFile.write('TeamName,HasLogo,HasJersey,HasCap\n')
allFiles = []
teamDict = {}

class PngFile:

    def __init__(self, t,fp, sp, teamName):
        self.type = t
        self.fullPath = fp
        self.shortPath = sp
        self.teamName = teamName

    def __str__(self):
        return self.type +' for ' + self.teamName

    def __repr__(self):
        return self.type +' for ' + self.teamName

#if not i.isdigit()
for u in glob.glob(path):


    #print('u', u)
    l = ''.join([let for let in u if  not let.isdigit()]).lower().replace(strippedpath.lower(), '').replace(' ','').replace('.png','').split('_')
    #print('l', l)
    #print('j', ' '.join([x.capitalize() for x in l]))
    #print('')
    j = ' '.join([x.capitalize() for x in l if (x <> 'small' and x <> 'alt' and x<> 'away')])

    if l[0] == 'caps':
        fileType = 'Cap'
        j = ' '.join([x.capitalize() for x in l[1:] if (x <> 'small' and x <> 'alt' and x<> 'away')])
    elif l[0] == 'jerseys':
        fileType = 'Jersey'
        j = ' '.join([x.capitalize() for x in l[1:] if (x <> 'small' and x<> 'alt' and x<> 'away')])
    else :
        fileType = 'Logo'

    p = PngFile(fileType, u, l, j)
    allFiles.append(p)


fSet = []
for f in allFiles:
    localSet = []
    JerseyFlag = 0
    CapFlag = 0
    for a in allFiles:
        if f <> a and f.type == 'Logo' and a.type <> 'Logo' and (f.teamName in a.teamName or a.teamName in f.teamName  ):
            #print(f.fullPath, a.fullPath)
            localSet.append(f.fullPath)
            localSet.append(a.fullPath)
            if a.type == 'Cap':
                CapFlag = 1

            if a.type == 'Jersey':
                JerseyFlag = 1

    if f.teamName not in teamDict:
        teamDict[f.teamName] = [f]
    else:
        teamDict[f.teamName].append(f)

    #if CapFlag + JerseyFlag > 0:
    #    print(f.teamName, CapFlag, JerseyFlag, localSet)

    if CapFlag>0 and JerseyFlag > 0:
        fSet += localSet

fSet = list(set(fSet))

for u in fSet:
    print(u)
    #os.rename(u, u.replace(strippedpath, strippedpath+'tryingtomove/'))
    print('Ready to move !!', u, u.replace(strippedpath, strippedpath+'tryingtomove/'))

for team in teamDict:
    s = team +','+ str(len([x for x in teamDict[team] if x.type == 'Logo'])) +',' + str(len([x for x in teamDict[team] if x.type == 'Jersey'])) + ',' + str(len([x for x in teamDict[team] if x.type == 'Cap'])) + '\n'
    LogoInfoFile.write(s)
    print(team, len([x for x in teamDict[team] if x.type == 'Logo']), len([x for x in teamDict[team] if x.type == 'Jersey']), len([x for x in teamDict[team] if x.type == 'Cap']))