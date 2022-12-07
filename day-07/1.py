from os.path import *

with open('day-07/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

curdir = '/'
files = {'/':0}

for item in data:
    item = item.rstrip()
    if item.startswith('$ cd'):
        curdir = abspath(join(curdir, item[5:]))
    elif item.startswith('dir'):
        files[join(curdir,item[4:])+'\\'] = 0
    elif item[0] != '$':
        size, fn = item.split()
        files[join(curdir,fn)] = int(size)

dirs = [key for key in files if key.endswith('\\')]
sizes = sorted([sum([size for fn,size in files.items() if fn.startswith(d)]) 
         for d in dirs])

total = 0
for size in sizes:
    if size < 100000:
        total += size
print("100000以下のファイルは合計",total)