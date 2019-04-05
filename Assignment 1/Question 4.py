# Prompt: Working with Files
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

def main():
	f = open('rosalind_ini5.txt', 'r')
	lines = f.readlines() #lines stored as list

	outfile = open('output.txt', 'w')
	for x in range (0,len(lines)):
		if (x%2==1):
			outfile.write(lines[x])

	f.close()
	outfile.close()

if __name__ == "__main__":
  main()