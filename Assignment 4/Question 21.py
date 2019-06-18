# Prompt: Compute the Forward of a String Emitted by an HMM
# Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
# Return: The Forward Pr(x) that the HMM emits x.

import numpy as np

def main():
# parsing files...
	f = open('rosalind_ba10j.txt', 'r')
	lines = f.readlines()
	num_iter = int(lines[0].strip()) # number of iterations
	emissionPath = lines[2].strip() # emitted path
	print("emissionPath:", emissionPath)

	emissions = lines[4].strip().replace("\t", "").replace(" ", "")
	print("emissions:", emissions)
	emit_dict = {}
	for i in range(len(emissions)):
		emit_dict[emissions[i]] = i
	
	states = lines[6].strip().replace("\t", "").replace(" ", "")
	print("states:", states)

# Initial Transition Matrix
	TM = []
	k = 9
	while lines[k].strip() != "--------":
		temp_tm = (lines[k].strip().split("\t"))[1:]
		temp_tm = [float(i) for i in temp_tm]
		TM.append(temp_tm) # append all values except for the 1st
		print(TM[k-9])
		k += 1

# Initial Emission Matrix
	k += 2 # get rid of the matrix title line
	EM = []
	for n in range(len(states)):
		temp_em = (lines[k].strip().split("\t"))[1:]
		temp_em = [float(i) for i in temp_em]
		EM.append(temp_em) # Ax is [0][0], Ay is [0][1], ..., Bx is [1][0] => i: states; j: emissions
		print(EM[n])
		k += 1

# HMM - Baum Welch
	# Construct Foward Matrix
	Forward = [[0 for j in range(len(states))] for i in range(len(emissionPath))] # column 0 for 'A', column 1 for 'B', etc.
	# initial Forward (1st column)
	for i in range(len(states)):
		Forward[0][i] += EM[i][emit_dict[emissionPath[0]]]
	# other probabilities
	for i in range(1, len(emissionPath)):
		for j in range(len(states)): # go through each *curr* state
			for prev in range(len(states)): # go through each *prev* state and sum up all probability
				Forward[i][j] += EM[j][emit_dict[emissionPath[i]]] * Forward[i-1][prev] * TM[prev][j]

	Forward_Sink_Pr = sum(Forward[len(emissionPath)-1])/2 # sum of the Forward of all states in the last column

	# Construct Backward Matrix
	Backward = [[0 for j in range(len(states))] for i in range(len(emissionPath))] # column 0 for 'A', column 1 for 'B', etc.
	# initial Backward (last column)
	for i in range(len(states)):
		Backward[len(emissionPath)-1][i] += EM[i][emit_dict[emissionPath[0]]]
	# other probabilities
	for i in range(len(emissionPath)-2, -1, -1): # backward calculation
		for j in range(len(states)): # go through each *curr* state
			for prev in range(len(states)): # go through each *prev* state and sum up all probability
				# print(EM[j][emit_dict[emissionPath[i]]])
				# print(Backward[i+1][prev])
				# print(TM[prev][j])
				Backward[i][j] += EM[j][emit_dict[emissionPath[i]]] * Backward[i+1][prev] * TM[prev][j]

	# Construct Node Responsible Matrix (Forward-Backward Algorithm)
	NMR = [[0 for j in range(len(states))] for i in range(len(emissionPath))]
	for i in range(len(emissionPath)):
		for j in range(len(states)): # go through each *curr* state
			NMR[i][j] = Forward[i][j] * Backward[i][j] / Forward_Sink_Pr
	
	for i in range(len(NMR)):
		for j in range(len(NMR[i])):
			if j != len(NMR[i])-1:
				print(str(NMR[i][j]), end = "	")
			else:
				print(NMR[i][j])

	# Construct Edge Responsible Matrix


if __name__ == "__main__":
  main()