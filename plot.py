import spellcheck
import matplotlib.pyplot as plt


#parse and divide wikitypo into typos truewords and
typos = list()
truewords = list()
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
		
errors = [0] * 444
#indexes = [0] * 444
for i in [0,1,2,4]:
	for j in [0,1,2,4]:
			for k in [0,1,2,4]:
				#deletion_cost = i
				#insertion_cost = j
				#substitution_cost = k
				combo = i * 100 + j * 10 + k
				#index[combo] = combo
				errors[combo] = spellcheck.measure_error(typos,truewords,dictionary,1,1,1)


plt.plot(errors,'ro')

plt.show()










