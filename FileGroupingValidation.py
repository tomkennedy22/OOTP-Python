from operator import itemgetter
path = '/Users/tom/OOTP Staging/_NeedsHelp/'

import glob
import os

helplist = []

filelist = glob.glob(path+'*')

op = []

for u in filelist:
    logoFlag = 0
    capFlag = 0
    jerseyFlag = 0
    if os.path.isdir(u):
        #print(u)
        for f in glob.glob(u + '/*'):
            #print(f)
            if f.find('jerseys') > 0:
                jerseyFlag = 1
                #print(f, 'is jersey')
            if f.find('caps') > 0:
                capFlag = 1
                #print(f, 'is cap')
            if f.find('jerseys') == -1 and f.find('caps') == -1:
                logoFlag = 1
                #print(f, 'is logo')
    else:
        continue

    op.append((u, logoFlag+capFlag+jerseyFlag))

    #print(u, logoFlag, capFlag, jerseyFlag)

op.sort(key=itemgetter(1), reverse=True)
for u in op:
    print(u)