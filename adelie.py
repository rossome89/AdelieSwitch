import subprocess
print "Welcome to AdelieSwitch!"
print "------------------------"
choiceConsole = raw_input("Which console would you like to change the controls for? ")
choicePlayer = raw_input("How many players would you like to use? Please enter 1 or 2 ")
if choiceConsole == "SNES" and choicePlayer == "1":
	SNES1 = raw_input('You would like to set the SNES to 1 Player. Is that correct?')
	if SNES1 == 'Yes':
		subprocess.call("snesplayer1", shell=True)
	else:
		print "Nevermind."
elif choiceConsole == "SNES" and choicePlayer == "2":
	SNES2 = raw_input('You would like to set the SNES to 2 Player. Is that correct?')
	if SNES2 == ('Yes'):
		subprocess.call("snesplayer2", shell=True)
	else:
		print "Nevermind."
else:
	print "I'm sorry, that's not supported yet."