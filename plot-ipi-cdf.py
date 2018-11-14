
import sys 

if len(sys.argv)<2:
	sys.exit("please pass the file name")
if len(sys.argv)<3:
	sys.exit("please pass the interval ex.10 or 100")


file_name = sys.argv[1]
N = int(sys.argv[2])
#N = 100

count_shoot = 0
flg_shoot = 0
base_shoot = 0
list_count_shoot = dict()

count_ipi = 0
flg_ipi = 0
base_ipi = 0
list_count_ipi = dict()

print("Couting shootdowns and ipis..... ")

with open(file_name,'r') as file:
	for line in file:
		t = line[34:].split(':')[0]
		t =t.split('.')[0] + t.split('.')[1][:3]
		if line.find("reason:remote shootdown") != -1:
			if flg_shoot == 0:
				flg_shoot = int(t)
				base_shoot = int(t)
				flg_ipi = int(t)
				base_ipi = int(t)
			if int(t)>base_shoot + N:
				list_count_shoot[base_shoot] = count_shoot
				base_shoot += N 
			while int(t)>base_shoot + N:
				list_count_shoot[base_shoot] = count_shoot
				base_shoot += N
			count_shoot+=1   
		elif line.find("reason:remote ipi send") != -1:
			#t = line[34:44].replace('.','')
			if flg_ipi == 0:
				flg_ipi = int(t)
				base_ipi = int(t)
				flg_shoot = int(t)
				base_shoot = int(t)
			if int(t)>base_ipi + N:
				list_count_ipi[base_ipi] = count_ipi
				base_ipi += N
			while int(t)>base_ipi + N:
				list_count_ipi[base_ipi] = count_ipi
				base_ipi += N
			count_ipi+=1

if count_ipi != 0:
	list_count_ipi[base_ipi] = count_ipi
if count_shoot != 0:
	list_count_shoot[base_shoot] = count_shoot


print("Done counting.")

values_shoot = []
keys_shoot = []
values_ipi = []
keys_ipi = []

for key in sorted(list_count_shoot.iterkeys()):
	values_shoot.append(list_count_shoot[key])
	keys_shoot.append(key - flg_shoot)

for key in sorted(list_count_ipi.iterkeys()):
	values_ipi.append(list_count_ipi[key])
	keys_ipi.append(key - flg_ipi)

import matplotlib.pyplot as plt

print("Ploting graphs.... ")
#plt.plot(list(list_count_shoot.keys()), list(list_count_shoot.values()) , label='Shootdowns')
#plt.plot(list(list_count_ipi.keys()), list(list_count_ipi.values()) , label="IPI's")
#plt.plot(keys_shoot , values_shoot ,'-bo', label = "Shootdown")
plt.plot(keys_ipi , values_ipi ,'-ro', label = "IPI")
plt.xlabel('Time normalized ('+str(flg_ipi) +')')
plt.legend()
plt.show()

