with open('day-01/input1') as file:
    data = [i for i in file.read().strip().split("\n")]

count = 0
index = 0
elf_list = []
for item in data:
        if item == '':
            elf_list.append(count)
            count = 0
            index +=1
        else:
            num = int(item)
            count += num

elf_list.sort(reverse=True)

print(elf_list)
print(elf_list[0])
print(elf_list[1])
print(elf_list[2])

elf_sum = elf_list[0] + elf_list[1] + elf_list[2]
print(elf_sum)