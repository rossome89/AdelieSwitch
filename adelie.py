import subprocess
# welcome message
print "Welcome to AdelieSwitch!"
print "------------------------"
# prompt for user input
choiceConsole = raw_input("Which console would you like to change the controls for? ").lower()
choicePlayer = raw_input("How many players would you like to use? Please enter 1 or 2: ").lower()
# process user input
#snes
if choiceConsole == "snes" and choicePlayer == "1":
		subprocess.call("snesplayer1", shell=True)
elif choiceConsole == "snes" and choicePlayer == "2":
		subprocess.call("snesplayer2", shell=True)
#megadrive
elif choiceConsole == "md" and choicePlayer == "1":
		subprocess.call("megadriveplayer1", shell=True)
elif choiceConsole == "md" and choicePlayer == "2":
		subprocess.call("megadriveplayer2", shell=True)
elif choiceConsole == "megadrive" and choicePlayer == "1":
		subprocess.call("megadriveplayer1", shell=True)
elif choiceConsole == "megadrive" and choicePlayer == "2":
		subprocess.call("megadriveplayer2", shell=True)
else:
	print "I'm sorry, that's not supported yet."