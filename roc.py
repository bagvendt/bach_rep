import numpy as np
import matplotlib.pyplot as plt

file = open('roc.csv', 'r').read()
lines = file.split('\n')

# Fra 3 til og med 12 og igen fra 15 til og med 24
recalls = []
precs = []

for i in range(3,13):
	values = lines[i].split(',')
	recall = values[2]
	prec = values[5]
	recalls.append(recall)
	precs.append(prec)
	
for i in range(15,25):
	values = lines[i].split(',')
	recall = values[2]
	prec = values[5]
	recalls.append(recall)
	precs.append(prec)

plt.plot(precs,recalls)


