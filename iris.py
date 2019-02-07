f = open('iris.csv')

data = []
labels = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2}

columns = f.readline().strip().split(',')[:4]

for line in f:
	l = line.strip().split(',')
	for i in range(4): l[i] = float(l[i])
	l[4] = labels[l[4]]
	data.append(l)
	
f.close()

print(data)
print(columns)

col1 = [i[0] for i in data]
col2 = [i[1] for i in data]
col3 = [i[2] for i in data]
col4 = [i[3] for i in data]
cols = [i[:4] for i in data]
targets = [i[4] for i in data]


'''
import numpy as np

labels = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2}
data = np.loadtxt('iris.csv', skiprows=1, delimiter=',',
		converters={4: lambda s: labels[s]}, encoding='latin-1')
		# np.loadtxt()'s default encoding is 'bytes'
		# 'utf-8', 'cp949'(windows default korean'), 'ascii', 'latin1', 'latin-1'

print(data)
'''