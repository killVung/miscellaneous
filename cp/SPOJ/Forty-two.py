import sys
import io

f = input()
while int(f) != 42:
	sys.stdout.write(str(f) + '\n')
	f = input()	