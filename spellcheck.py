import csv
import matplotlib.pyplot as plt
import time
import sys

#get the deletion, insertion and substitution cost

#deletion_cost = float(sys.argv[1])
#insertion_cost = float(sys.argv[2])
#substitution_cost = float(sys.argv[3])

infile_name = sys.argv[1]
dictionary_name = sys.argv[2]
typos = list()
#truewords = list()

def parse_infile (infile_name):

	with open(infile_name) as infile:
		for raw in infile:
			raw_list = raw.split("\t")
			typos.append(raw_list[0])
			typos.append(raw_list[1])

def parse_dict (dictionary_name):
	with open(dictionary_name) as dictionary:
		for raw in dictionary:
			raw_list = raw.split("\r\n")#raw.split("\r\n")
			dictionary.append(raw_list[0])







def find_closest_word (string1, dictionary, deletion_cost, insertion_cost, substitution_cost):
	min_dist = 999999999999999999999999999 #a really large initial distance to begin with
	for s in dictionary:
		dist = levenshtein_distance(string1, s, deletion_cost, insertion_cost, substitution_cost) # deletion,sub,insertion costs are 1
		if dist < min_dist:
			min_dist = dist
			closest_word = s
	return closest_word



def levenshtein_distance(string1, string2, deletion_cost, insertion_cost, substitution_cost):
	import numpy as np
	d = np.zeros((len(string1)+1,len(string2)+1))#, dtype=numpy.int
	for i in range(len(string1)+1):
		d[i, 0] = i * deletion_cost
	for j in range(len(string2)+1):
		d[0, j] = j * insertion_cost
		
	for jj in range(1, len(string2)+1):
		for ii in range(1, len(string1)+1):
			if string1[ii-1] == string2[jj-1]:
				d[ii,jj] = d[ii-1,jj-1] #no operation cost
			else:
				d[ii,jj] = min(d[ii-1, jj] + deletion_cost,
							   d[ii, jj-1] + insertion_cost,
							   d[ii-1, jj-1] + substitution_cost)
	
	return d[len(string1),len(string2)]
	

#print(find_closest_word("zog",["dog","fyz","www"]))

def measure_error(typos, truewords, dictionarywords, deletion_cost, insertion_cost, substitution_cost):
	numerror = 0
	i = 0
	for typo in typos:
		closest_word = find_closest_word(typo,dictionarywords, deletion_cost, insertion_cost, substitution_cost)
		if closest_word != truewords[i]:
			numerror = numerror + 1
		i = i + 1
		
			
	return float(numerror) / float(len(typos))
	
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



def qwerty_levenshtein_distance(string1, string2, deletion_cost, insertion_cost):
	import numpy as np
	d = np.zeros((len(string1)+1,len(string2)+1))#dtype=numpy.int
	for i in range(len(string1)+1):
		d[i, 0] = i * deletion_cost
	for j in range(len(string2)+1):
		d[0, j] = j * insertion_cost
		
	for jj in range(1, len(string2)+1):
		for ii in range(1, len(string1)+1):
			if string1[ii-1] == string2[jj-1]:
				d[ii,jj] = d[ii-1,jj-1] #no operation cost
			else:
				d[ii,jj] = min(d[ii-1, jj] + deletion_cost,
							   d[ii, jj-1] + insertion_cost,
							   d[ii-1, jj-1] + qwerty_distance(string1[ii-1], string2[jj-1]))
	
	return d[len(string1),len(string2)]
	

#print(measure_error(["flee","lovv","dib"],["flea","loss","job"],["dogg","flea","wqdq","dog"]))

#parse and divide wikitypo into typos truewords and
#typos = list()
#truewords = list()
with open("cleantypo.txt","rb") as infile:
	for raw in infile:
		raw_list = raw.split()
		typos.append(raw_list[0])
		truewords.append(raw_list[1])
#print(typos)
#print(truewords)


#parse the dictionary
dictionary = list()
with open("clean.txt","rb") as dictfile:
	for raw in dictfile:
		raw_list = raw.split("\n")#raw.split("\r\n")
		dictionary.append(raw_list[0])
		
#print(dictionary)


#start = time.time()

#print("The error is")
#print(measure_error(typos,truewords,dictionary))

#print(time.time()-start)
