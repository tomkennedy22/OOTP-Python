import glob
import os


staging = []
prod = []
for u in glob.glob('/Users/tom/OOTP Staging/*'):
    #print(u)
    lu = u.split('/')
    x = lu[-1]
    #print(u,x)
    staging.append(x)

for u in glob.glob('/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/logos/*.png'):
    #print(u)
    lu = u.split('/')
    x = lu[-1]
    #print(u,x)
    prod.append(x)

for u in glob.glob('/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/jerseys/*.png'):
    #print(u)
    lu = u.split('/')
    x = lu[-1]
    #print(u,x)
    prod.append(x)

for u in glob.glob('/Users/tom/Library/Application Support/Out of the Park Developments/OOTP Baseball 19/ballcaps/*.png'):
    #print(u)
    lu = u.split('/')
    x = lu[-1]
    #print(u,x)
    prod.append(x)

staging.sort()

for u in staging:
    if u in prod:
        print(u)
        os.rename('/Users/tom/OOTP Staging/'+u, '/Users/tom/OOTP Staging/_'+u)