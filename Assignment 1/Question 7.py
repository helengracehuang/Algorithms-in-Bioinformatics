# Prompt: Enumerating k-mers Lexicographically
# Assume that an alphabet 𝒜 has a predetermined order; that is, we write the alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).
# Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in 𝒜.
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
def main():
	collection = "A C G T"
	n = 2
	alphabet = collection.split(' ') # split the collection by individual characters
	
	# combination = []
	# for x in range (0, len(alphabet)):
	# 	combination[x] = alphabet[x]


	# for x in range (0, len(alphabet)):
	# 	for i in range (0, len(alphabet)):
	# 		# if alphabet[x] != alphabet[i]:
	# 		print(alphabet[x]+alphabet[i])

if __name__ == "__main__":
  main()