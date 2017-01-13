
# bear_moved = False
# while True:
# 	next = raw_input(">")
# 	if next == "take honey":
# 		dead("The bear looks at you then slaps your face off.")
# 	elif next == "taunt bear" and not bear_moved:
# 		print "The bear has moved from the door.You can go through it now."
# 		bear_moved = True
# 	elif next == "taunt bear" and bear_moved:
# 		dead("The bear gets pissed off and chews your leg off.")
# 	elif next == "open door" and bear_moved:
# 		gold_room()
# 	else:
# 		print "I got no idea what that means."


bear_moved = False
while True:
	next = "taunt"
	if next == "take honey":
		dead("The bear looks at you then slaps your face off.")
	elif next == "taunt bear" and not bear_moved:
		print "The bear has moved from the door.You can go through it now."
		bear_moved = True
	elif next == "taunt bear" and bear_moved:
		dead("The bear gets pissed off and chews your leg off.")
	elif next == "open door" and bear_moved:
		gold_room()
	else:
		print "I got no idea what that means."