from msvcrt import getch
import os
import sys
import colorama

colorama.init()
move = 0
move_lr = 0
window_opened = False
options = ['Option1', 'Option2', 'Option3', 'Exit']


def getKey():
        global move, move_lr, window_opened
	# 27 - esc
	# 72 - up Arrow
	# 80 - down Arrow
	# 77 - right key
	# 75 - left key
	key = ord(getch())
	if key == 27: quit()
	if key == 72:
		if window_opened != True:
			if move <= 0:
				move = 0
				pass
			else: move -= 1
			menu(move)
	if key == 80:
		if window_opened != True:
			if move >= len(options) - 1:
				move = len(options) - 1
				pass
			else: move += 1
			menu(move)
	if key == 77:
		move_lr = -1
		window_opened = True
		print_content(move)
	if key == 75:
		move_lr = 1
		window_opened = False
		menu(move)
		
def menu(choice):
	os.system('cls')
	sys.stdout.write("\033[32m\t\tWelcome!\n\033[0m")
	for i in range(len(options)):
		if i == choice:
			sys.stdout.write('\033[36m\t-> \033[0m{}\n'.format(options[i]))
		else: print '\t   {}'.format(options[i])

def print_content(choice):
	if choice == (len(options) - 1):
		quit("\t\tAdios!")
	else:
		os.system('cls')
		print "\033[32m\t\tWelcome! - {}\033[0m".format(options[choice])
		with open("{}.txt".format(options[choice]), 'r') as f:
			print f.read()
		sys.stdout.write("\n\033[31mExit\033[0m \033[36m<-\n\033[0m")
	move_lr = 0

menu(move)
while True:
	getKey()
