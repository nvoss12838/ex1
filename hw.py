hw =  'Hello World, Actually New lines are better'
f = open('helloworld.txt','w')
for letter in hw:
	f.write(letter.capitalize()+'\t')
#H	E	L	L	O...
f.close()

