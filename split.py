
file_list = ['dict/index.adj','dict/index.adv','dict/index.noun','dict/index.verb']
d = dict()

for file_index in file_list:
	f = open(file_index)
	index = 0
	while True :
		i = f.readline()
		if i=='': break
		reg = i.split()	
		if index>=29 and reg[0] not in d:
			#print(reg[0])
			d[reg[0]] = -1
		index += 1
	f.close()

f = open('output.txt', 'w')
for i in iter(d):
	f.write(i+"\n")
f.close()
print('Done.')




