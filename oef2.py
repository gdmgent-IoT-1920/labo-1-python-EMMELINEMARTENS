# lees een document en loop de woorden 

docs = open("namen.txt")

d = dict()

for doc in docs:
	doc = doc.strip()
	if doc in d:
		d[doc] = d[doc] + 1
	else:
		d[doc] = 1
for key in list(d.keys()):
	print('{}:{}'.format(key,d[key]))

docs.close()

