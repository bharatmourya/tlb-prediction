
import sys 

if len(sys.argv)<2:
	sys.exit("please pass the file name")
if len(sys.argv)<3:
	sys.exit("please pass the interval ex.10 or 100")


file_name = sys.argv[1]
N = int(sys.argv[2])
#N = 100

'''count_shoot = 0
flg_shoot = 0
base_shoot = 0
list_count_shoot = dict()

count_ipi = 0
flg_ipi = 0
base_ipi = 0
list_count_ipi = dict()
'''
list_count_shoot = dict()
base_shoot = 0
count_shoot = 0

print("Couting shootdowns and ipis..... ")

vadd = dict()

with open(file_name,'r') as file:
	for line in file:
		t = line[9:].split(' ')[0]
		time = int(t.split(':')[0])*60 + int(t.split(':')[1].replace('.',''))
		if line.find("munmap(0x") != -1:
			t = line[32:50]
			if t in vadd:
				vadd[t] += 1
			else:
				vadd[t] = 1

for key,value in vadd.items():
	print key,": ",value
