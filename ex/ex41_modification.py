from sys import exit
from random import randint

def death():
	quips = ["You died.You kinda suck at this.",
			"Nice job,you died ... jackass.",
			"Such a luser.",
			"I have a small puppy that's better at this."]
	print quips[randint(0,len(quips)-1)]
	exit(1)

def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew."
	print "You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,"
	print "put it in the bridge, and blow the ship up after getting into an escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when a Gothon down jumps out, red scaly skin, dark grimy teeth, "
	print "and evil clown costume flowing around his hate filled body."
	print "He's blocking the door to the Armory and about to pull a weapon to blast you."
	print "shoot!,dodge!,tell a joke?"
	action = raw_input(">")
	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body, which throws off your aim."
		print "Your laser hits his costume but misses him entirely ."
		print "This completely ruins his brand new costume his mother bought him, "
		print "which makes him fly into an insane rage and blast you repeatedly in the face until you are dead."
		print "Then he eats you."
		return 'death'
	elif action == 'dodge!':
		print "Like a world class boxer you dodge ,weave,slip and slide right as the Gothon's blaster cranks a laser past your head."
		print "In the middle of your artful dodge your foot slips and you bang your head on the matal wall and pass out."
		print "You wake up shortly after only to die as the Gothon stomps on bang your head on the matal wall and pass out."
		return 'death'
	elif action == "tell a joke":
		print "Lucky for you they made you learn Gothon insults in the academy."
		print "You tell the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sng,jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhfr."
		print "The Gothon stops,tries not to laugh,then busts out laughing and can't move."
		print "while he's laughing you run up and shoot him square in the head putting him down,"
		print "then jump through the Weapon Armory door."
		return "laser_weapon_armory"
	else:
		print "DOES NOT COMPUTE!"
		return 'central_corridor'

def laser_weapon_armory():
	print "You do a dive roll into the Weapon Armory,crouch and scan the room for more Gothon that might be hiding."
	print "It's dead quiet,too quiet."
	print "You stand up and run to the far side of the room and find the neutron bomb in its container."
	print "There's a keypad lock on the box and you need the code to get the bomb out. "
	print "If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits."
	code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]>")
	guesses = 0
	while guess != code and guesses < 10:
		print "BZZZZEDDD!"
		guesses += 1
		guess = raw_input("[keypad]>")
	if guess == code:
		print "The container clicks open and the seal breaks,letting gas out. "
		print "You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot. "
		return 'the_bridge'
	else:
		print "The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together."
		print "You decide to sit there,and finally the Gothons blow up the ship from their ship and you die."
		return 'death'

def the_bridge():
	print "You burst onto the Bridge with the neutron destruct bomb under your arm and don't want to set it off."
	action = raw_input(">")
	if action == "throw the bomb":
		print "In a panic you throw the bomb at the group of Gothons and make a leap for the door."
		print "Right as you drop it a Gothon shoots you right in the back killing you."
		print "As you die you see another Gothon frantically try to disarm the bomb."
		print "You die knowing they will probably blow up when it goes off."
		return 'death'
	elif action == "slowly place the bomb":
		print "You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat."
		print "You inch backward to the door,open it ,and then carefully place the bomb on the floor,pointing your blaster at it."
		print "You then jump back through the door,punch the close button and blast the lock so the Gothons can't get out."
		print "Now that the bomb is placed you run to the escape pod to get off this tin can."
		return 'escape_pod'
	else:
		print "DOES NOT COMPUTE!"
		return "the_bridge"

def escape_pod():
	print "You rush through the ship desperately trying to make it to  the escape pod before the whole ship explodes."
	print "It seems like hardly any Gothons are on the ship,so your run is clear of interference."
	print "You get to the chamber with the escape pods,and now need to pick one to take. "
	print "Some of them could be damaged but you don't have time to lock. "
	print "There's 5 pods, which one do you take?"
	good_pod = randint(1,5)
	guess = raw_input("[pod #]>")
	if int(guess) != good_pod:
		print "You jump into pod %s and hit the eject button."% guess
		print "The pod escapes out  into the void of space,then implodes as the hull ruptures,"
		print "crushing your body into jam jelly"
		return 'death'
	else:
		print "You jump into pod %s and hit the eject button."% guess
		print "The pod easily slides out into space heading to the planet below."
		print "As it flies to the planet,you look back and see your ship implode then explode like a brights star,"
		print "taking out the Gothon ship at the same time."
		print "You won!"
		exit(0)

ROOMS = {
	'death':death,
	'central_corridor':central_corridor,
	'laser_weapon_armory':laser_weapon_armory,
	'the_bridge':the_bridge,
	'escape_pod':escape_pod
}

def runner(map,start):
	next = start
	while True:
		room = map[next]
		print "\n----------"
		next = room()

runner(ROOMS,'central_corridor')









































