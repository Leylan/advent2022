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
sizes = [sum([size for fn,size in files.items() if fn.startswith(d)]) 
         for d in dirs]
basedirs = [key for key in files if key.count('\\') == 2 and key.endswith('\\')]
root = sum([sum([size for fn,size in files.items() if fn.startswith(d)]) 
         for d in basedirs])

required_space = 30000000 - (70000000 - root)
matches = []
for size in sizes:
    if size > required_space:
        matches.append(size)
best_match = min(matches)        
print("スペースを十分空にするには一番サイズに適切するファイルは",best_match)
sizes.pop()