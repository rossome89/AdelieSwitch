import subprocess
print "Welcome to AdelieSwitch!"
print "------------------------"
choiceConsole = raw_input("Which console would you like to change the controls for? ")
choicePlayer = raw_input("How many players would you like to use? Please enter 1 or 2: ")
if choiceConsole == "SNES" and choicePlayer == "1":
		subprocess.call("snesplayer1", shell=True)
elif choiceConsole == "SNES" and choicePlayer == "2":
		subprocess.call("snesplayer2", shell=True)
elif choiceConsole == "snes" and choicePlayer == "1":
		subprocess.call("snesplayer1", shell=True)
elif choiceConsole == "snes" and choicePlayer == "2":
		subprocess.call("snesplayer2", shell=True)
else:
	print "I'm sorry, that's not supported yet."