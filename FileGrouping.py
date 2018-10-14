path = '/Applications/MAMP/htdocs/CFB-Realignment/img/TeamLogos/'

import glob
import os

def Is_Hex(str):
    if str.__len__() != 6:
        return False

    try:
        int(str, 16)
        return True
    except ValueError:
        return False

helplist = []

filelist = glob.glob(path+'*')

filelist = sorted(filelist)

for u in filelist:
    print(u)
    spl = u.replace('.png', '').replace(path, '').split('_')
    if spl.__len__() > 1:

        if  Is_Hex(spl[-2]) == True and Is_Hex(spl[-1]) == True:
            print('is hex!')
            newpath = u.replace('_'+spl[-2], '').replace('_'+spl[-1], '')
            print('new apth', newpath)
            os.rename(u, newpath)


    # if not u.endswith('png'):
    #     continue
    # print('\n**********************')
    # print( u.replace(path,''))
    # print(u.replace(path,'').replace('jerseys_','').replace('caps_',''))
    # x = input()
    # l = u.replace(path,'').replace('jerseys_','').replace('caps_','').replace('.png','').split('_')
    # if x > 0:
    #     folderpath = '_'.join(l[:x])
    #     print(u, 'belongs to ', folderpath)
    #     if not os.path.exists(path+folderpath):
    #         os.makedirs(path+folderpath)
    #     os.rename(u, path+folderpath+'/'+u.replace(path,''))
    # else:
    #     helplist.append(u)

print(helplist)