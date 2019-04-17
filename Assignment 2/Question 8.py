# Prompt: Find the Length of a Longest Path in a Manhattan-like Grid
# Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.
# Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.
import numpy as np

def ManhattanTourst(n, m, Down, Right):
	Path = np.empty((n+1, m+1))
	Path[0][0] = 0
	for i in range(1, n+1):
		Path[i][0] = Path[i-1][0] + Down[i-1][0]
	for j in range(1, m+1):
		Path[0][j] = Path[0][j-1] + Right[0][j-1]
	for i in range(1, n+1):
		for j in range(1, m+1):
			Path[i][j] = max(Path[i-1][j]+Down[i-1][j], Path[i][j-1]+Right[i][j-1])
	# 		print(i,j,Path[i][j])
	# print(Path[n][m])
	return (Path[n][m])

def main():
	n, m = 18, 5 # CHANGE this according to the data
	f = open('rosalind_ba5b.txt', 'r')
	lines = f.readlines()
	i = 1 # read from the second line
	downMatrix = []
	rightMatrix = []
	while lines[i] != '-\n': # read in down matrix until the '-'
		# print(i, (lines[i].rstrip()).split(' '))
		intLine = (lines[i].rstrip()).split(' ')
		intLine = [int(k) for k in intLine]
		downMatrix.append(intLine)
		i += 1
	i += 1 # skip the '-'
	while i < len(lines): # read in right matrix after the '-'
		intLine = (lines[i].rstrip()).split(' ')
		intLine = [int(k) for k in intLine]
		rightMatrix.append(intLine)
		i += 1
	# print(downMatrix)
	# print(rightMatrix)

	print(int(ManhattanTourst(n, m, downMatrix, rightMatrix)))

if __name__ == "__main__":
  main()