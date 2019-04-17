# Prompt: Multiple Alignment
# Given: A collection of four DNA strings of length at most 10 bp in FASTA format.
# Return: A multiple alignment of the strings having maximum TotalScore, where we TotalScore matched symbols 0 (including matched gap symbols) and all mismatched symbols -1 (thus incorporating a linear gap penalty of 1).
import numpy as np
import sys

def Score(a, b, c, d):
	score = 0
	if a != b:
		score -= 1
	if a != c:
		score -= 1
	if a != d:
		score -= 1
	if b != c:
		score -= 1
	if b != d:
		score -= 1
	if c != d:
		score -= 1
	return score

def TotalScore(str1, str2, str3, str4):
	global TSM
	global Backtrack

	TSM = np.zeros([len(str1)+1, len(str2)+1, len(str3)+1, len(str4)+1], dtype = int)
	Backtrack = np.zeros([len(str1)+1, len(str2)+1, len(str3)+1, len(str4)+1], dtype = int)

	TSM[0][0][0][0] = 0
	Backtrack[0][0][0][0] = 0

	for i in range(1, len(str1)+1):
		TSM[i][0][0][0] = TSM[i-1][0][0][0]-3 # indel penalty = -1
		Backtrack[i][0][0][0] = 1
	for j in range(1, len(str2)+1):
		TSM[0][j][0][0] = TSM[0][j-1][0][0]-3 # indel penalty = -1
		Backtrack[0][j][0][0] = 2
	for k in range(1, len(str3)+1):
		TSM[0][0][k][0] = TSM[0][0][k-1][0]-3 # indel penalty = -1
		Backtrack[0][0][k][0] = 3
	for l in range(1, len(str4)+1):
		TSM[0][0][0][l] = TSM[0][0][0][l-1]-3 # indel penalty = -1
		Backtrack[0][0][0][l-1] = 4

	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			TSM[i][j][0][0] = max(
				TSM[i-1][j][0][0]-3,
				TSM[i][j-1][0][0]-3, 
				TSM[i-1][j-1][0][0]+Score(str1[i-1], str2[j-1], '-', '-'))
			if TSM[i][j][0][0] == TSM[i-1][j][0][0]-3:
				Backtrack[i][j][0][0] = 1
			elif TSM[i][j][0][0] == TSM[i][j-1][0][0]-3:
				Backtrack[i][j][0][0] = 2
			elif TSM[i][j][0][0] == TSM[i-1][j-1][0][0]+Score(str1[i-1], str2[j-1], '-', '-'):
				Backtrack[i][j][0][0] = 5
	for i in range(1, len(str1)+1):
		for k in range(1, len(str3)+1):
			TSM[i][0][k][0] = max(
				TSM[i-1][0][k][0]-3,
				TSM[i][0][k-1][0]-3, 
				TSM[i-1][0][k-1][0]+Score(str1[i-1], '-', str3[k-1], '-'))
			if TSM[i][0][k][0] == TSM[i-1][0][k][0]-3:
				Backtrack[i][0][k][0] = 1
			elif TSM[i][0][k][0] == TSM[i][0][k-1][0]-3:
				Backtrack[i][0][k][0] = 3
			elif TSM[i][0][k][0] == TSM[i-1][0][k-1][0]+Score(str1[i-1], '-', str3[k-1], '-'):
				Backtrack[i][0][k][0] = 6
	for i in range(1, len(str1)+1):
		for l in range(1, len(str4)+1):
			TSM[i][0][0][l] = max(
				TSM[i-1][0][0][l]-3,
				TSM[i][0][0][l-1]-3, 
				TSM[i-1][0][0][l-1]+Score(str1[i-1], '-', '-', str4[l-1]))
			if TSM[i][0][0][l] == TSM[i-1][0][0][l]-3:
				Backtrack[i][0][0][l] = 1
			elif TSM[i][0][0][l] == TSM[i][0][0][l-1]-3:
				Backtrack[i][0][0][l] = 4
			elif TSM[i][0][0][l] == TSM[i-1][0][0][l-1]+Score(str1[i-1], '-', '-', str4[l-1]):
				Backtrack[i][0][0][l] = 7
	for j in range(1, len(str2)+1):
		for k in range(1, len(str3)+1):
			TSM[0][j][k][0] = max(
				TSM[0][j-1][k][0]-3,
				TSM[0][j][k-1][0]-3, 
				TSM[0][j-1][k-1][0]+Score('-', str2[j-1], str3[k-1], '-'))
			if TSM[0][j][k][0] == TSM[0][j-1][k][0]-3:
				Backtrack[0][j][k][0] = 2
			elif TSM[0][j][k][0] == TSM[0][j][k-1][0]-3:
				Backtrack[0][j][k][0] = 3
			elif TSM[0][j][k][0] == TSM[0][j-1][k-1][0]+Score('-', str2[j-1], str3[k-1], '-'):
				Backtrack[0][j][k][0] = 8
	for j in range(1, len(str2)+1):
		for l in range(1, len(str4)+1):
			TSM[0][j][0][l] = max(
				TSM[0][j-1][0][l]-3,
				TSM[0][j][0][l-1]-3, 
				TSM[0][j-1][0][l-1]+Score('-', str2[j-1], '-', str4[l-1]))
			if TSM[0][j][0][l] == TSM[0][j-1][0][l]-3:
				Backtrack[0][j][0][l] = 2
			elif TSM[0][j][0][l] == TSM[0][j][0][l-1]-3:
				Backtrack[0][j][0][l] = 4
			elif TSM[0][j][0][l] == TSM[0][j-1][0][l-1]+Score('-', str2[j-1], '-', str4[l-1]):
				Backtrack[0][j][0][l] = 9
	for k in range(1, len(str3)+1):
		for l in range(1, len(str4)+1):
			TSM[0][0][k][l] = max(
				TSM[0][0][k-1][l]-3,
				TSM[0][0][k][l-1]-3, 
				TSM[0][0][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]))
			if TSM[0][0][k][l] == TSM[0][0][k-1][l]-3:
				Backtrack[0][0][k][l] = 3
			elif TSM[0][0][k][l] == TSM[0][0][k][l-1]-3:
				Backtrack[0][0][k][l] = 4
			elif TSM[0][0][k][l] == TSM[0][0][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]):
				Backtrack[0][0][k][l] = 10
	for j in range(1, len(str2)+1):
		for k in range(1, len(str3)+1):
			for l in range(1, len(str4)+1):
				i = 0
				TSM[0][j][k][l] = max(
						TSM[0][j-1][k][l]-3, 
						TSM[0][j][k-1][l]-3, 
						TSM[0][j][k][l-1]-3,
						TSM[0][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'), 
						TSM[0][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]), 
						TSM[0][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]),
						TSM[0][j-1][k-1][l-1]+Score('-', str2[j-1], str3[k-1], str4[l-1]))
				if TSM[0][j][k][l] == TSM[i][j-1][k][l]-3:
					Backtrack[0][j][k][l] = 2
				elif TSM[0][j][k][l] == TSM[i][j][k-1][l]-3:
					Backtrack[0][j][k][l] = 3
				elif TSM[0][j][k][l] == TSM[i][j][k][l-1]-3:
					Backtrack[0][j][k][l] = 4
				elif TSM[i][j][k][l] == TSM[i][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'):
					Backtrack[i][j][k][l] = 8
				elif TSM[i][j][k][l] == TSM[i][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]):
					Backtrack[i][j][k][l] = 9
				elif TSM[i][j][k][l] == TSM[i][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]):
					Backtrack[i][j][k][l] = 10
				elif TSM[i][j][k][l] == TSM[i][j-1][k-1][l-1]+Score('-', str2[j-1], str3[k-1], str4[l-1]):
					Backtrack[i][j][k][l] = 11
	for i in range(1, len(str1)+1):
		for k in range(1, len(str3)+1):
			for l in range(1, len(str4)+1):
				j = 0
				TSM[i][j][k][l] = max(
						TSM[i-1][j][k][l]-3,
						TSM[i][j][k-1][l]-3, 
						TSM[i][j][k][l-1]-3, 
						TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'), 
						TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]),
						TSM[i][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]),
						TSM[i-1][j][k-1][l-1]+Score(str1[i-1], '-', str3[k-1], str4[l-1]))
				if TSM[i][j][k][l] == TSM[i-1][j][k][l]-3:
					Backtrack[i][j][k][l] = 1
				elif TSM[i][j][k][l] == TSM[i][j][k-1][l]-3:
					Backtrack[i][j][k][l] = 3
				elif TSM[i][j][k][l] == TSM[i][j][k][l-1]-3:
					Backtrack[i][j][k][l] = 4
				elif TSM[i][j][k][l] == TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'):
					Backtrack[i][j][k][l] = 6
				elif TSM[i][j][k][l] == TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]):
					Backtrack[i][j][k][l] = 7
				elif TSM[i][j][k][l] == TSM[i][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]):
					Backtrack[i][j][k][l] = 10
				elif TSM[i][j][k][l] == TSM[i-1][j][k-1][l-1]+Score(str1[i-1], '-', str3[k-1], str4[l-1]):
					Backtrack[i][j][k][l] = 12
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			for l in range(1, len(str4)+1):
				k = 0
				TSM[i][j][k][l] = max(
					TSM[i-1][j][k][l]-3, 
					TSM[i][j-1][k][l]-3,
					TSM[i][j][k][l-1]-3, 
					TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'), 
					TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]),  
					TSM[i][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]), 
					TSM[i-1][j-1][k][l-1]+Score(str1[i-1], str2[j-1], '-', str4[l-1]))
				if TSM[i][j][k][l] == TSM[i-1][j][k][l]-3:
					Backtrack[i][j][k][l] = 1
				elif TSM[i][j][k][l] == TSM[i][j-1][k][l]-3:
					Backtrack[i][j][k][l] = 2
				elif TSM[i][j][k][l] == TSM[i][j][k][l-1]-3:
					Backtrack[i][j][k][l] = 4
				elif TSM[i][j][k][l] == TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'):
					Backtrack[i][j][k][l] = 5
				elif TSM[i][j][k][l] == TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]):
					Backtrack[i][j][k][l] = 7
				elif TSM[i][j][k][l] == TSM[i][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]):
					Backtrack[i][j][k][l] = 9
				elif TSM[i][j][k][l] == TSM[i-1][j-1][k][l-1]+Score(str1[i-1], str2[j-1], '-', str4[l-1]):
					Backtrack[i][j][k][l] = 13

	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			for k in range(1, len(str3)+1):
				l = 0
				TSM[i][j][k][l] = max(
					TSM[i-1][j][k][l]-3, 
					TSM[i][j-1][k][l]-3, 
					TSM[i][j][k-1][l]-3, 
					TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'), 
					TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'),
					TSM[i][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'),
					TSM[i-1][j-1][k-1][l]+Score(str1[i-1], str2[j-1], str3[k-1], '-'))
				
				if TSM[i][j][k][l] == TSM[i-1][j][k][l]-3:
					Backtrack[i][j][k][l] = 1
				elif TSM[i][j][k][l] == TSM[i][j-1][k][l]-3:
					Backtrack[i][j][k][l] = 2
				elif TSM[i][j][k][l] == TSM[i][j][k-1][l]-3:
					Backtrack[i][j][k][l] = 3
				elif TSM[i][j][k][l] == TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'):
					Backtrack[i][j][k][l] = 5
				elif TSM[i][j][k][l] == TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'):
					Backtrack[i][j][k][l] = 6
				elif TSM[i][j][k][l] == TSM[i][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'):
					Backtrack[i][j][k][l] = 8
				elif TSM[i][j][k][l] == TSM[i-1][j-1][k-1][l]+Score(str1[i-1], str2[j-1], str3[k-1], '-'):
					Backtrack[i][j][k][l] = 14

	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			for k in range(1, len(str3)+1):
				for l in range(1, len(str4)+1):
					TSM[i][j][k][l] = max(
						TSM[i-1][j][k][l]-3, 
						TSM[i][j-1][k][l]-3, 
						TSM[i][j][k-1][l]-3, 
						TSM[i][j][k][l-1]-3, 
						TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'), 
						TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'), 
						TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]), 
						TSM[i][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'), 
						TSM[i][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]), 
						TSM[i][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]),
						TSM[i][j-1][k-1][l-1]+Score('-', str2[j-1], str3[k-1], str4[l-1]),
						TSM[i-1][j][k-1][l-1]+Score(str1[i-1], '-', str3[k-1], str4[l-1]),
						TSM[i-1][j-1][k][l-1]+Score(str1[i-1], str2[j-1], '-', str4[l-1]),
						TSM[i-1][j-1][k-1][l]+Score(str1[i-1], str2[j-1], str3[k-1], '-'),
						TSM[i-1][j-1][k-1][l-1]+Score(str1[i-1], str2[j-1], str3[k-1], str4[l-1]))
					
					if TSM[i][j][k][l] == TSM[i-1][j][k][l]-3:
						Backtrack[i][j][k][l] = 1
					elif TSM[i][j][k][l] == TSM[i][j-1][k][l]-3:
						Backtrack[i][j][k][l] = 2
					elif TSM[i][j][k][l] == TSM[i][j][k-1][l]-3:
						Backtrack[i][j][k][l] = 3
					elif TSM[i][j][k][l] == TSM[i][j][k][l-1]-3:
						Backtrack[i][j][k][l] = 4

					elif TSM[i][j][k][l] == TSM[i-1][j-1][k][l]+Score(str1[i-1], str2[j-1], '-', '-'):
						Backtrack[i][j][k][l] = 5
					elif TSM[i][j][k][l] == TSM[i-1][j][k-1][l]+Score(str1[i-1], '-', str3[k-1], '-'):
						Backtrack[i][j][k][l] = 6
					elif TSM[i][j][k][l] == TSM[i-1][j][k][l-1]+Score(str1[i-1], '-', '-', str4[l-1]):
						Backtrack[i][j][k][l] = 7
					elif TSM[i][j][k][l] == TSM[i][j-1][k-1][l]+Score('-', str2[j-1], str3[k-1], '-'):
						Backtrack[i][j][k][l] = 8
					elif TSM[i][j][k][l] == TSM[i][j-1][k][l-1]+Score('-', str2[j-1], '-', str4[l-1]):
						Backtrack[i][j][k][l] = 9
					elif TSM[i][j][k][l] == TSM[i][j][k-1][l-1]+Score('-', '-', str3[k-1], str4[l-1]):
						Backtrack[i][j][k][l] = 10

					elif TSM[i][j][k][l] == TSM[i][j-1][k-1][l-1]+Score('-', str2[j-1], str3[k-1], str4[l-1]):
						Backtrack[i][j][k][l] = 11
					elif TSM[i][j][k][l] == TSM[i-1][j][k-1][l-1]+Score(str1[i-1], '-', str3[k-1], str4[l-1]):
						Backtrack[i][j][k][l] = 12
					elif TSM[i][j][k][l] == TSM[i-1][j-1][k][l-1]+Score(str1[i-1], str2[j-1], '-', str4[l-1]):
						Backtrack[i][j][k][l] = 13
					elif TSM[i][j][k][l] == TSM[i-1][j-1][k-1][l]+Score(str1[i-1], str2[j-1], str3[k-1], '-'):
						Backtrack[i][j][k][l] = 14
					elif TSM[i][j][k][l] == TSM[i-1][j-1][k-1][l-1]+Score(str1[i-1], str2[j-1], str3[k-1], str4[l-1]):
						Backtrack[i][j][k][l] = 15
	return(TSM[len(str1)][len(str2)][len(str3)][len(str4)])

def Output(bt, str1, str2, str3, str4, i, j, k, l):
	global Backtrack
	global outputstr1
	global outputstr2
	global outputstr3
	global outputstr4

	if i == 0 and j == 0 and k == 0 and l == 0:
		return
	if Backtrack[i][j][k][l] == 1:
		Output(bt, str1, str2, str3, str4, i-1, j, k, l)
		outputstr1 += str1[i-1]
		outputstr2 += '-'
		outputstr3 += '-'
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 2:
		Output(bt, str1, str2, str3, str4, i, j-1, k, l)
		outputstr1 += '-'
		outputstr2 += str2[j-1]
		outputstr3 += '-'
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 3:
		Output(bt, str1, str2, str3, str4, i, j, k-1, l)
		outputstr1 += '-'
		outputstr2 += '-'
		outputstr3 += str3[k-1]
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 4:
		Output(bt, str1, str2, str3, str4, i, j, k, l-1)
		outputstr1 += '-'
		outputstr2 += '-'
		outputstr3 += '-'
		outputstr4 += str4[l-1]

	elif Backtrack[i][j][k][l] == 5:
		Output(bt, str1, str2, str3, str4, i-1, j-1, k, l)
		outputstr1 += str1[i-1]
		outputstr2 += str2[j-1]
		outputstr3 += '-'
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 6:
		Output(bt, str1, str2, str3, str4, i-1, j, k-1, l)
		outputstr1 += str1[i-1]
		outputstr2 += '-'
		outputstr3 += str3[k-1]
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 7:
		Output(bt, str1, str2, str3, str4, i-1, j, k, l-1)
		outputstr1 += str1[i-1]
		outputstr2 += '-'
		outputstr3 += '-'
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 8:
		Output(bt, str1, str2, str3, str4, i, j-1, k-1, l)
		outputstr1 += '-'
		outputstr2 += str2[j-1]
		outputstr3 += str3[k-1]
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 9:
		Output(bt, str1, str2, str3, str4, i, j-1, k, l-1)
		outputstr1 += '-'
		outputstr2 += str2[j-1]
		outputstr3 += '-'
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 10:
		Output(bt, str1, str2, str3, str4, i, j, k-1, l-1)
		outputstr1 += '-'
		outputstr2 += '-'
		outputstr3 += str3[k-1]
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 11:
		Output(bt, str1, str2, str3, str4, i, j-1, k-1, l-1)
		outputstr1 += '-'
		outputstr2 += str2[j-1]
		outputstr3 += str3[k-1]
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 12:
		Output(bt, str1, str2, str3, str4, i-1, j, k-1, l-1)
		outputstr1 += str1[i-1]
		outputstr2 += '-'
		outputstr3 += str3[k-1]
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 13:
		Output(bt, str1, str2, str3, str4, i-1, j-1, k, l-1)
		outputstr1 += str1[i-1]
		outputstr2 += str2[j-1]
		outputstr3 += '-'
		outputstr4 += str4[l-1]
	elif Backtrack[i][j][k][l] == 14:
		Output(bt, str1, str2, str3, str4, i-1, j-1, k-1, l)
		outputstr1 += str1[i-1]
		outputstr2 += str2[j-1]
		outputstr3 += str3[k-1]
		outputstr4 += '-'
	elif Backtrack[i][j][k][l] == 15:
		Output(bt, str1, str2, str3, str4, i-1, j-1, k-1, l-1)
		outputstr1 += str1[i-1]
		outputstr2 += str2[j-1]
		outputstr3 += str3[k-1]
		outputstr4 += str4[l-1]
	# print("i=", i, "j=", j, "k=", k, "l=", l, "bt=", Backtrack[i][j][k][l])

def main():
	global TSM
	global outputstr1
	global outputstr2
	global outputstr3
	global outputstr4
	global Backtrack

	s1 = "TGCAGTTT"
	s2 = "GGGGCTAA"
	s3 = "TTTGGACTA"
	s4 = "TACAGTTAGT"

	print(TotalScore(s1, s2, s3, s4))

	outputstr1 = ""
	outputstr2 = ""
	outputstr3 = ""
	outputstr4 = ""

	Output(Backtrack, s1, s2, s3, s4,len(s1), len(s2), len(s3), len(s4))
	print(outputstr1)
	print(outputstr2)
	print(outputstr3)
	print(outputstr4)

if __name__ == "__main__":
  main()