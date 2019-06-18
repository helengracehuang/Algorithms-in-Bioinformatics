# Prompt: Compute the Probability of a String Emitted by an HMM
# Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
# Return: The probability Pr(x) that the HMM emits x.

import numpy as np

def main():
	# parsing files...
	f = open('rosalind_ba10d.txt', 'r')
	lines = f.readlines()
	# emissionPath = "zxzzzxzxzxzyxzxxzxyzzzzxxxyxyzyyzyyxzxxxxzxyxyxxyxzzzxzxyzxyxzxzyzyzxxxyzxxyyzyzyyyzxyxyzzzyzzxxzxyx"
	emissionPath = lines[0].strip()
	print("emissionPath:", emissionPath)

	emissions = lines[2].strip().replace("\t", "").replace(" ", "")
	print("emissions:", emissions)
	emit_dict = {}
	for i in range(len(emissions)):
		emit_dict[emissions[i]] = i
	
	states = lines[4].strip().replace("\t", "").replace(" ", "")
	print("states:", states)

	# Transition Matrix
	# TM = [[1 for i in range(len(states))] for j in range(len(states))]
	TM = []
	k = 7
	while lines[k].strip() != "--------":
		temp_tm = (lines[k].strip().split("\t"))[1:]
		temp_tm = [float(i) for i in temp_tm]
		TM.append(temp_tm) # append all values except for the 1st
		print(TM[k-7])
		k += 1

	# Emission
	k += 2 # get rid of the matrix title line
	EM = []
	for n in range(len(states)):
		temp_em = (lines[k].strip().split("\t"))[1:]
		temp_em = [float(i) for i in temp_em]
		EM.append(temp_em) # Ax is [0][0], Ay is [0][1], ..., Bx is [1][0] => i: states; j: emissions
		print(EM[n])
		k += 1


	# HMM - Viterbi
	probability = [[0 for i in range(len(states))] for j in range(len(emissionPath))] # column 0 for 'A', column 1 for 'B', etc.
	# record = [[-1 for i in range(len(states))] for j in range(len(emissionPath))] # backtracking

	# initial probability
	for i in range(len(states)):
		probability[0][i] += EM[i][emit_dict[emissionPath[0]]]

	# other probabilities
	for i in range(1, len(emissionPath)):
		for j in range(len(states)): # go through each *curr* state
			for prev in range(len(states)): # go through each *prev* state and pick the most probable curr state
				probability[i][j] += EM[j][emit_dict[emissionPath[i]]] * probability[i-1][prev] * TM[prev][j]
				# record[i][j] = prev # record the prev state curr comes from


	output = sum(probability[len(emissionPath)-1]) # sum of the probability of all states in the last colum

	print(output/2)

if __name__ == "__main__":
  main()