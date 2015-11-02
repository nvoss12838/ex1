hw =  'Hello World, Actually New lines are better'
f = open('helloworld.txt','w')
for letter in hw:
	f.write(letter.capitalize()+ '\n')
f.close()

