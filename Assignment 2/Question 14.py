# Prompt: Generate the Last-to-First Mapping of a String
# Given: A string Transform and an integer i.
# Return: The position LastToFirst(i) in FirstColumn in the Burrows-Wheeler matrix if LastColumn = Transform.

bp_counts = {'A':0, 'C':0, 'G':0, 'T':0} # initialize a dictionary of A,T,C,G => '$'' must be the 1st
standard_gene = "ACGT"
global ref_encoded

def bw_count():
	global ref_encoded

	for i in range(len(ref_encoded)):
		try:
			bp_counts[ref_encoded[i]] += 1
		except:
			continue
# end bw_count()

def LastToFirst(i, encoded): # Apply Burrows-Wheeler transform to input string
	return bw_getPartRank(encoded[i]) + bw_getRank_ch(i, encoded[i], encoded)

def bw_getPartRank(nucleotide): # sum up number of items before current group of nucleotide
	rank = 0 # the (position 0) is always '$' !!!!!!!!!!!!!!!!
	for i in range(3):
			if standard_gene[i] < nucleotide:
				rank += bp_counts[standard_gene[i]]
			else:
				break
	# print("bw_getPartRank:",rank)
	return rank

def bw_getRank_ch(index, nucleotide, encoded): # return the rank of "nucleotide" within the same characters
	rank = 1 # base case
	if index == 0:
		return 1
	if encoded[index-1]==nucleotide:
		rank = bw_getRank_ch(index-1, nucleotide, encoded) + 1
	else:
		rank = bw_getRank_ch(index-1, nucleotide, encoded)
	# print("bw_getRank_ch:",rank)
	return rank
# end bw_getRank_ch()

def main():
	global ref_encoded

	ref_encoded = "GTAAGGATTGACTATTGCGCGGACGGGTTACTCAGCAAGCCTAGAGCTGGTTTATTGACATCAAGTAGTCATGTCATTGTCATTTTTGACAGCTTCGAGATATCGACATAGGAGGTACTGATGCTATCGACGCTAGTTCTGTCACGAAGCTGTGGTCCGACTTGCAACAGGGTAGTCTAGTTCTGCGTGTTAGTAGAGCTCAAGTGAGCCTGATACTTCGTATCCTTTAAATCACACAGGCTTTCTAGTCGCTTAGTGAGCTCAACATAAGACTGAATCGCGACTCAAGTATTCAACAGCAGTTTTCCTCTACTGCGCTGGATTGAGCTGGGCAGCGCAAGGATAGTGTTGAGTAGACCAGATGTAGGTAGACTCAGCGTTGGAATCTTGGGATCGATCAGGTATCGGTGAAAGATAGCAGACGGTCATTCAATTATCTTTACTGCTCGATCGGGTTAACGCCCGCGCTCACACAATGGAGTTAATTAATCCATAGTGTCAAGGTTCCTCGTGGCGAGGGGGTTCCGATTCATCCGCGGAGGAGGTACAAGTAATTAACATGCTCTCTATATGTTCGTTGAGGGACCCGGCAGCAAGGATTTAGGAGTACCAAAGCACCCGTTCCGCGACCAAGCTCACAACGTGATGGCCATTCAAGGTAAAGCGGGCGCACAACGGTCTTTCCGGCATTTAGACGGTTGTCCCATCTCCCGTATTTAGTTTGCAGCACGCAGTGCGGGATCAAGCTGCAGTGAGCCCATCAAACTAATTTTGCTTCGGGTGTAGAGAATTTTTTGCAACCCTTCAGGAGCTGCAGGGTCGCCTAAGAAAGGTTCGCCTGTAGCAGTGTTCTTGGTACTTATAGATCCCCTGAAGGAATCAGGGTTGTAAATAGGGGG$"
	position = 101 #integer i

	bw_count()
	print(LastToFirst(position, ref_encoded))

if __name__ == "__main__":
  main()