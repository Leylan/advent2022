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

elf_sum = elf_list[0] + elf_list[1] + elf_list[2]
print('最もカロリーを持っているエルフのトップ３は合計',elf_sum,'カロリーを持っている')