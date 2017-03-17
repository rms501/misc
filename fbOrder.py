import random

playerMap = {
	1:'Rob',
	2:'Joe',
	3:'Matt',
	4:'Justin',
	5:'Dave',
	6:'Erich',
	7:'Joyce',
	8:'Nick',
	9:'Derek',
	10:'Andy'
}

order = []

while(playerMap):

	draw = random.randint(1,10)

	if draw in playerMap.keys():
		order.append(playerMap.pop(draw))

count = 1
for i in order:
	print('Pick ', count, ': ', i)
	count += 1