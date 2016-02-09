import sys
import random

MAX_LOOP = 10
MIN_GEN = 10
MAX_GEN = 100


# #Generate n sets with range from 10 to n
# def gen_rand_tree():	
# 	i = 10
# 	while i != 1000000:
# 		for j in range(i):
# 			#Generate two random numbers in the range 
# 			random.randint(1,i)

w = sys.stdout

for s in range(MAX_LOOP):
	i,j = [random.randint(MIN_GEN,MAX_GEN),random.randint(MIN_GEN,MAX_GEN)]	
	while (i % 10 > 10):
		i,j = [random.randint(MIN_GEN,MAX_GEN),random.randint(MIN_GEN,MAX_GEN)]

	w.write(str(i) + " " + str(j) + "\n")







