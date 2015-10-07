def qwerty_distance(item1, item2):
	import numpy as np
	if item1 == item2:
		return 0
	q1 = ["1","2","3","4","5","6","7","8","9","0"]
	q2 = ["q","w","e","r","t","y","u","i","o","p"]
	q3 = ["a","s","d","f","g","h","j","k","l","dumy"]
	q4 = ["z","x","c","v","b","n","m","dumy","dumy","dumy"]
	
	keyboard = np.array([q1,q2,q3,q4])
	item1 = item1.lower()
	item2 = item2.lower()	
	for i in range(np.shape(keyboard)[0]):
		for j in range(np.shape(keyboard)[1]):
			if keyboard[i][j] == item1:
				pos1 = [i,j]
			if keyboard[i][j] == item2:
				pos2 = [i,j]
	
	dis = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
	
	return dis

print(qwerty_distance('Q','d'))



