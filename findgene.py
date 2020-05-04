import sys
import getopt
import re
def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'i:o:s')
	except getopt.GetoptError as err:
		sys.exit(2)

	fileIn = ""
	outFile = ""
	inp = 0
	out = 0
	a = ""

	for (opt, arg) in opts:
		if (opt == '-i'):
			fileIn = fileIn + arg
			inp = 1
		if (opt == '-o'):
			out = 1
			outFile = outFile + arg

	if (inp == 0):
		fileIn = fileIn + input("Input file to read from: ")

	readFile = open(fileIn, "r")

	def findGene(lineIn):
		lineOut = ""
		for i in range(len(lineIn)):
			if (lineIn[i] == 'g' and lineIn[i+1] == 'e' and lineIn[i+2] == 'n' and lineIn[i+3] == 'e' and lineIn[i+4] == '='):
				n = i
				while (lineIn[n+5] != ']'):
					lineOut = lineOut + lineIn[n+5]
					n += 1	
		return lineOut
	
	line = readFile.readline()
	while (line):
		if (findGene(line) != ""):
			a = a + findGene(line) + "\n"
			line = readFile.readline()
		else:
			line = readFile.readline()
	readFile.close()
	
	if (out == 0):
		print(a)
	else:
		writeOut = open(outFile, "w")
		writeOut.write(a)
		writeOut.close()

if __name__ == "__main__":
	main()
