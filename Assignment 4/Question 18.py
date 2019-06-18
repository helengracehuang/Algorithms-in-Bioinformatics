# Prompt: Compute the Probability of an Outcome Given a Hidden Path
# Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
# Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.

def main():
	emissionPath = "yyzyzxxxyxzyyzzzxzyxyyyyxyyyxyzyyyzxxyxzxxxyyyxyzx"
	hiddenPath = "BAAAABBABBBBBBBBBABBABAABAABBBBBBABAAABBABABBABBBB"
	Ax = 0.225
	Ay = 0.098
	Az = 0.678
	Bx = 0.84
	By = 0.02
	Bz = 0.14
	probability = 1
	for i in range(len(hiddenPath)):
		if hiddenPath[i] == 'A' and emissionPath[i] == 'x':
			probability *= Ax
		elif hiddenPath[i] == 'A' and emissionPath[i] == 'y':
			probability *= Ay
		elif hiddenPath[i] == 'A' and emissionPath[i] == 'z':
			probability *= Az
		elif hiddenPath[i] == 'B' and emissionPath[i] == 'x':
			probability *= Bx
		elif hiddenPath[i] == 'B' and emissionPath[i] == 'y':
			probability *= By
		elif hiddenPath[i] == 'B' and emissionPath[i] == 'z':
			probability *= Bz
	print(probability)

if __name__ == "__main__":
  main()