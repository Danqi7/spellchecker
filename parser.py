import sys

dictionary = list()
with open("clean.txt","rb") as dictfile:
	for raw in dictfile:
		raw_list = raw.split("\n")
		dictionary.append(raw_list[0])
		print(raw)
		
print(dictionary)