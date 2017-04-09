from msvcrt import getch
import os
move = 0

def getKey():
	global move
	#print move
	# 27 - esc
	# 72 - up Arrow
	# 80 - down Arrow
	key = ord(getch())
	if key == 27: quit()
	if key == 72:
		if move <= 0:
			move = 0
			pass
		else: move -= 1
		menu(move)
	if key == 80:
		if move >= 2:
			move = 2
			pass
		else: move += 1
		menu(move)

def menu(choice):
	options = ['Option1', 'Option2', 'Option3']
	os.system('cls')
	for i in range(len(options)):
		if i == choice:
			print '\t-> {}'.format(options[i])
		else: print '\t   {}'.format(options[i])

while True:
	getKey()
	#menu(move)
