from pydub import AudioSegment
import owl_artwork
import ovo_functions
import time
import os


# ///Main Loop///

while 1:

	# //Welcome Screen//
	print owl_artwork.ovo_owl_image
	time.sleep(1)
	print "Welcome to OVO Sound Generator!"
	time.sleep(1.5)
	
	# //User Input//
	user_input = raw_input("""
	Select one of the following options:
		1. Reverse sample
		2. Underwater effect

	To exit the program, type "exit".
	""")

	# //Reverse Sample//
	if user_input == str(1):
		os.system('clear')
		time.sleep(.5)
		print """
REVERSE SAMPLE

		"""
		time.sleep(1)
		ovo_functions.reverse_sample()
		break

	# //Underwater Effect//
	elif user_input == str(2):
		os.system('clear')
		time.sleep(.5)
		print """
UNDERWATER EFFECT

		"""
		time.sleep(1)
		ovo_functions.underwater_effect()
		break

	# //Exit//
	elif user_input.lower() == "exit":
		time.sleep(1)
		print """

	Goodbye!
"""
		break