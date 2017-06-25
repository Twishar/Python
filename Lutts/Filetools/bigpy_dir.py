#отычскивает наибольший файл с исходным программным кодом (в 1 каталоге)

import os, glob, sys
dirname = r'E:\Python\Python\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')

for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])

