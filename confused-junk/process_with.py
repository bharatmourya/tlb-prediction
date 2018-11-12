import re

f = open('tlb_with.txt', 'r')
fw = open('with.gnu','w')

total_per_sec=[]
tlb_rate=[]

for line in f.readlines():
    processed_line=re.sub(' +',' ',line)
    data=processed_line.split(' ')[1:9]
    int_data=map(int, data)
    total_per_sec.append(sum(int_data))


without_gnu_data=[x - total_per_sec[i - 1] for i, x in enumerate(total_per_sec)][1:]

for item in without_gnu_data:
    fw.write(str(item)+'\n')

f.close()
