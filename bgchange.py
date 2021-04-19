#!/usr/bin/python
# Import all the services we'll need
import sys
import os
import subprocess
import random
import time

# Make sure we have all the cli args we need
try:
	# The first argument passed in the cli - how long to wait between background changes
	seconds_to_wait = int(sys.argv[1])
	# The second argument passed in the cli - where all the backgrounds are
	path_to_backgrounds = sys.argv[2]
except:
	# Not enough args passed
	print("Not enough arguments passed")
	# Exit the program
	exit()

# Declare some variables we'll need later
current_background = ""
prev_background = ""
feh_command = ""

# While this is running
while(True):
	# Set the previous background to the current one so we don't repeat two in a row
	prev_background = current_background
	# Keep selecting a new random background from the directory until it's different from the last
	while(prev_background == current_background):
		# Set the current background to a new random one
		current_background = random.choice(os.listdir(path_to_backgrounds))
		# Wait a little so we don't overload the processor
		time.sleep(0.25)
	# Generate the command to execute
	feh_command = ["feh", "--no-fehbg", "--image-bg", "black", "--bg-max", path_to_backgrounds + current_background]
	# Execute the command
	subprocess.run(feh_command)
	# Wait the chosen amount of time to refresh the background
	time.sleep(seconds_to_wait)
