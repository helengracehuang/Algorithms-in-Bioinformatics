# Prompt: Reconstruct a String from its Burrows-Wheeler Transform
# Given: A string Transform (with a single "$" sign).
# Return: The string Text such that BWT(Text) = Transform.

def bw_decoder(r): # Apply inverse Burrows-Wheeler transform
    temp_list_2 = [""] * len(r)  # Make empty list
    for i in range(len(r)):
        temp_list_2 = sorted(r[i] + temp_list_2[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in temp_list_2 if row.endswith("$")][0]  # Find the correct row (ending in ETX)
    # return s.rstrip("$")  # Get rid of end marker
    return s
# end bw_decoder()

def main():
	encoded_ref = "ATGATAATTTAGAACAAAAGCGAGTCGGGAACGGCTATAGATTTGGGCGCGCGGTTGCCACAGCCATAAACTAAAACGTGCAGAAAGTTATTTCCATTATAACTGGGGAACTTCCAGCCACGACGGCTCCTCGTAGTCGGTGTGTCATCCTCCTGCGACCATGGGGAATAGTTGCATGGGGGTCGCAGGGGACACTATCAATCACTCCCTGAAACAACCTAGGGCGGCCCAGCTGGTGGCATTGAATACGTAAATGAACTTCCCGTTCCATAATGTACAGTAATACAGATACCCATTATGATGCTGGAAGTCCTACCTTGTAGGATACCTGGACCGTTTTTGTCGCCACCACCTTCTGTCCGAAGGAAAATGTGAGAAGCCCCTTGGCGTCGGGAGTGCGGCACGATTGTTTGACGCTCAGGCGATCATTCGCAGCGGCAGTCGGAACTAAG$CCCAGTAGATACACCTGACTAGGTAATTGCGGTGAGCTCAAATGATGTTTAGCCGCGAGCTTGTAACCCGCGTGTTTTTATGGCACGCAGAGAACCGACGACCTTGTTCAATAAATCCCACGATCACTGCTTTTAGCCATGCAATATACCCGCTGTTCAGAAATTACAAACGTTAGAAATAGAATGCGGGGAAAAAGGACGGACTTTTGCGGGACGCGACCCATAAATACATTCCATAGAGCCCATTTATACGGTTACCAACGTTAAACTGGTGAAACAGGGAAGATTGACTATCGGCGCGACATGTTTCGGACTATTGTTAAACTCAGAAGAACAGATGTCAGCACGTCCAGGCGATCTAACGGATCGCCGCCATAGTCCGCCTCGCATACGCGTATGCGATGAAAATCGCGAGTCCGAACATGCCTGTATTTTGGTTTCAGGGACATTC"
	decoded_ref = bw_decoder(encoded_ref)
	print(decoded_ref)

if __name__ == "__main__":
  main()