
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
flg_shoot = 0

print("Couting shootdowns and ipis..... ")

with open(file_name,'r') as file:
	for line in file:
		t = line[9:].split(' ')[0]
		time = int(t.split(':')[0])*60 + int(t.split(':')[1].replace('.',''))
		time /= 1000
		if line.find("munmap(0x") != -1:
			if flg_shoot == 0:
				base_shoot = time
				flg_shoot = time
			if time>base_shoot + N:
				list_count_shoot[base_shoot] = count_shoot
				count_shoot = 0
				base_shoot += N 
			while time>base_shoot + N:
				list_count_shoot[base_shoot] = count_shoot
				base_shoot += N
			count_shoot+=1   



'''if count_ipi != 0:
	list_count_ipi[base_ipi] = count_ipi
if count_shoot != 0:
	list_count_shoot[base_shoot] = count_shoot
'''

print("Done counting.")

'''values_shoot = []
keys_shoot = []
values_ipi = []
keys_ipi = []

for key,value in list_count_shoot.items():
	values_shoot.append(value)
	keys_shoot.append(key - flg_shoot)

for key,value in list_count_ipi.items():
	values_ipi.append(value)
	keys_ipi.append(key - flg_ipi)
'''

values_shoot = []
keys_shoot = []

for key in sorted(list_count_shoot.keys()):
	values_shoot.append(list_count_shoot[key])
	keys_shoot.append(key - flg_shoot)


import matplotlib.pyplot as plt

print("Ploting graphs.... ")
#plt.plot(list(list_count_shoot.keys()), list(list_count_shoot.values()) , label='Shootdowns')
#plt.plot(list(list_count_ipi.keys()), list(list_count_ipi.values()) , label="IPI's")
plt.plot(keys_shoot , values_shoot ,'-bo', label = "Munmap")
#plt.plot(keys_ipi , values_ipi ,'-ro', label = "IPI")
plt.xlabel('Time normalized ('+str(flg_shoot) +')')
plt.legend()
plt.show()
