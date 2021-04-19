#!/usr/bin/python
# This kills any bgchange.py's that are running and sets it to a static background
import sys
import subprocess

try:
	# Get the name of the background to set
	background_path = sys.argv[1]
except:
	# No cli args
	print("Not enough arguments")
	# Exit the program
	exit()

# Generate the first command
get_pid_command = ["pgrep", "bgchange.py"]
# Get the pid of any running bgchange.py
pid_proc = subprocess.Popen(get_pid_command, stdout=subprocess.PIPE)
# Wait for the pid command to finish
pid_proc.wait()

# Kill all instances of bgchange
for line in iter(pid_proc.stdout.readline, b''):
	# Generate the kill command
	kill_bgchange_command = ["kill", line.rstrip()]
	# Execute the kill command
	kill_proc = subprocess.Popen(kill_bgchange_command)
	# Wait for the kill to finish
	kill_proc.wait()

# Generate the feh command
set_bg_command = ["feh", "--no-fehbg", "--image-bg", "black", "--bg-max", background_path]
# Execute the feh command
feh_proc = subprocess.Popen(set_bg_command)
feh_proc.wait()

