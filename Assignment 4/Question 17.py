# Prompt: Compute the Probability of a Hidden Path Problem
# Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).
# Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.

def main():
	hiddenPath = "BBBABBABBBABBABBABBABABBBABABBAABBABBABBABABAABABA"
	AtoA = 0.526
	AtoB = 0.474
	BtoA = 0.905
	BtoB = 0.095
	probability = 1
	for i in range(len(hiddenPath)):
		if i == 0:
			probability *= 0.5
		else:
			if hiddenPath[i-1] == 'A' and hiddenPath[i] == 'A':
				probability *= AtoA
			elif hiddenPath[i-1] == 'A' and hiddenPath[i] == 'B':
				probability *= AtoB
			elif hiddenPath[i-1] == 'B' and hiddenPath[i] == 'A':
				probability *= BtoA
			elif hiddenPath[i-1] == 'B' and hiddenPath[i] == 'B':
				probability *= BtoB
	print(probability)

if __name__ == "__main__":
  main()