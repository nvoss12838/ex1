hw =  'Hello World'
f = open('helloworld.txt','w')
for letter in hw:
	f.write(letter.capitalize()+ '\n')
f.close()

