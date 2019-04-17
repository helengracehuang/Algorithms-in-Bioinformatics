# Prompt: Implement BWMatching
# Given: A string BWT(Text), followed by a collection of strings Patterns.
# Return: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
import sys

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

def bw_search(t, encoded): # Traverse through the encoded string and find the range of locations
	# base case
	k = len(t)-1 #0,1,2,... => walk-left
	curr = t[k] # A,C,G,T
	if bp_counts[curr] == 0:
		return 0
	l_bound = bw_getPartRank(curr) + 1 # init lower bound
	u_bound = bw_getPartRank(curr) + bp_counts[curr] # init upper bound, two "pointers" to represent range
	# print("l_bound init:",l_bound)
	# print("u_bound init:",u_bound)
	while (k > 0):
		k -= 1
		curr = t[k]
		old_lb = 0
		while True:
			# print("encoded[l_bound] is:",encoded[l_bound])
			if encoded[l_bound] == curr:
				if k != 0: # if k is already 0, then don't change l_bound
					old_lb = l_bound
					l_bound = LastToFirst(l_bound, encoded)
					# print("l_bound new:",l_bound)
				break
			else:
				l_bound += 1 # not match, shrink range
				# print("l_bound change to:",l_bound)
				if l_bound > u_bound:
					return 0 # no match at all
		while True:
			if encoded[u_bound] == curr:
				if k != 0: # if k is already 0, then don't change u_bound
					u_bound = LastToFirst(u_bound, encoded)
					# print("u_bound new:",u_bound)
				break
			else:
				u_bound -= 1 # not match, shrink range
				if u_bound < old_lb:
					return 0 # no match at all
		if k == 0: # traversed through the entire t and found the match
			return u_bound-l_bound+1 # return the range of locations of t
	return 0
# end bw_search()

### encoded[index] = nucleotide, Therefore param: nucleotide is not needed, but included to save time (hopefully)

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

def bw_getRank_sa(index, nucleotide, encoded): # return the suffix index of the current "index"
	if nucleotide == '$':
		return -1 # $ is always the last one
	else:
		temp_idx = bw_getPartRank(nucleotide) + bw_getRank_ch(index, nucleotide, encoded)
		index = bw_getRank_sa(temp_idx, encoded[temp_idx], encoded) + 1
		return index

def bw_getRank_ch(index, nucleotide, encoded): # return the rank of "nucleotide" within the same characters
	rank = 1 # base case
	if index == 0:
		return 1
	if encoded[index-1]==nucleotide:
		rank = bw_getRank_ch(index-1, nucleotide, encoded) + 1
	else:
		rank = bw_getRank_ch(index-1, nucleotide, encoded)
	return rank

def main():
	global ref_encoded

	sys.setrecursionlimit(100000)

	f = open('rosalind_ba9l.txt', 'r')
	lines = f.readlines()
	# ref_encoded = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
	ref_encoded = lines[0].rstrip()
	# stringPatterns = "CCT CAC GAG CAG ATC"
	stringPatterns = lines[1]
	patterns = (stringPatterns.rstrip()).split(' ')

	bw_count()

	outfile = open('output.txt', 'w')
	for i in range(len(patterns)):
		outfile.write(str(bw_search(patterns[i], ref_encoded)))
		if i != len(patterns)-1:
			outfile.write(" ")

if __name__ == "__main__":
  main()