#This was coded and built using a Raspberry Pi model B.
#You will need 4 leds, 4 ressitors 270ohms, 4 resistors 10000ohms, 4 push buttons and jumper wires.
#Run this from the LX terminal.(sudo python memory_pi.py)
import RPi.GPIO as GPIO
import time
import random

#The order of buttons and leds can be changed to suit your personal preference.
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)#Button one
GPIO.setup(8, GPIO.IN)#Button two
GPIO.setup(25, GPIO.IN)#Button three
GPIO.setup(24, GPIO.IN)#Button four
GPIO.setup(23, GPIO.OUT)#led one
GPIO.setup(22, GPIO.OUT)#led two
GPIO.setup(27, GPIO.OUT)#led three
GPIO.setup(17, GPIO.OUT)#led four

#Here are the various variable neede to allow the code to function.
highscore_name = ["Farley"]
highscore_value = [12]
inputs = []
leds = [ 23,22,27,17]
pos = 0
delay = 0.5
#Values below are used to append to list to check same order. The starting order is below.
a = 23#led one
b= 22
c = 27
d = 17
leds_values = [a,b,c,d]	#Starting position leds for first flash.
number_of_flashes = 4 #Starting at four as we have four leds connected.

#Beginning the game.
print(" ")#These just print blank lines, it makes it look a bit better!
print("Let`s get ready to play!")
print(" ")
player_name = str(raw_input("Please enter your name: "))
print(" ")
play = str(raw_input("Push y to start, watch the flashes. Push the buttons in the same order:  "))
print(" ")	 

#First set of flahes.
for flash in range(0,len(leds)): 
	GPIO.output(leds[pos], GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(leds[pos], GPIO.LOW)
	time.sleep(delay)
	pos += 1
	if pos >= 4:
		pos = 0

#This function checks to see if input is correct and asks the player if they want to continue.
def check():
	global leds
	global inputs
	global number_of_flashes
	okay = 0
	for value in range(0,len(inputs)):
		if inputs[value] == leds[okay]:
			okay += 1
		#print(okay)
	if okay == len(leds):
		print(" ")
		for got_it in range(0,10):
			print("You got it!")
		print(" ")
		player_choice = str(raw_input("Do you want to take the next challenge, y or n: "))
		print(" ")
		if player_choice == 'y':
			number_of_flashes += 1
			inputs = []
			shuffle_leds(number_of_flashes)
		elif player_choice != 'y':
			if number_of_flashes > highscore_value[-1]:
				highscore_value.append(number_of_flashes)
				highscore_name.append(player_name)
				print(" ")
				print("HIGHSCORE %s FLASHES BY %s" % (highscore_value[-1], highscore_name[-1]))
				print(" ")
			elif number_of_flashes <= highscore_value:
				print(" ")
				print("HIGHSCORE %s FLASHES BY %s" % (highscore_value[-1], highscore_name[-1]))
				print(" ")
			exit()
	elif okay != len(leds):
		print(" ")
		for wrong in range(0,10):
			print("Sorry wrong answer!!!")
		print(" ")
		player_choice = str(raw_input("Do you want to try again, y or n: "))
		print(" ")
		if player_choice == 'y':
			inputs = []
			flash()
		elif player_choice != 'y':
			if number_of_flashes > highscore_value[-1]:
				highscore_value.append(number_of_flashes)
				highscore_name.append(player_name)
				print(" ")
				print("HIGHSCORE %s FLASHES BY %s" % (highscore_value[-1], highscore_name[-1]))
				print(" ")
			elif number_of_flashes <= highscore_value:
				print(" ")
				print("HIGHSCORE %s FLASHES BY %s" % (highscore_value[-1], highscore_name[-1]))
				print(" ")
			exit()
				
#This function puts the LEDs in a random order. Then calls flash().
def shuffle_leds(n):#This takes an argument, it can be increased as the game is played.
	global leds     #It will increase the number of times the leds flash.
	global led_values
	leds = []#We need to first empty the list.
	#print("Empty")
	#print(leds)
	for shuffle in range(0,n):#Add new random positions, assign led value. Finally add to list.
		position = random.randint(0,3)
		add_to_leds = leds_values[position]
		leds.append(add_to_leds)
	#print("New list")
	#print(leds)
	flash()

#This function is called by the above function. It flashes the new led list.
def flash():
	global pos
	for flash in range(0,len(leds)): 
		GPIO.output(leds[pos], GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(leds[pos], GPIO.LOW)
		time.sleep(delay)
		pos += 1
		if pos >= len(leds):#Resets pos back to zero after the flashes are completed.
			pos = 0

#Main loop, button pushes are checked here and appended to inputs list.
while True:
	
	if len(inputs) < len(leds):
		if (GPIO.input(7) == True):
			print("Button one pushed")
			time.sleep(.2)
			inputs.append(a)
			#print(inputs)
		elif (GPIO.input(8) == True):
			print("Button two pushed")
			time.sleep(.2)
			inputs.append(b)
			#print(inputs)
		elif (GPIO.input(25) == True):
			print("Button three pushed")
			time.sleep(.2)
			inputs.append(c)
			#print(inputs)
		elif (GPIO.input(24) == True):
			print("Button four pushed")
			time.sleep(.2)
			inputs.append(d)
			#print(inputs)
#When inputs reach the length of the check function is called.
	elif len(inputs) == len(leds):
		check()
#Handles if inputs goes over the length of leds list, could change above code to include this.
	elif len(inputs) > len(leds):
			check()
	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
