# Prompt: Strings and Lists
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

def main():
	s = "r7RlgkGeJ9QZ6Mg7GwJpGRApxSg3RuW4Fs3bkQJ2XyXIFwbaq7byhJBDh4TKr9TCHydrochelidon8n2BZqKnYZQavnw6FE51jHeiRD5z18OLAJqlNjKLerFXQa6NNOd6TLgiCM6PmurinussfT87eQBnNoZ6A4K7c9NcdOPWcKZL811guOhqrOUcD2UmbfnHafHo."
	a, b, c, d = 64, 76, 137, 143

	s1 = s[a:b+1] # list data structure!
	# for x in range (a, b+1):
	# 	s1 = s1 + s[x]

	s2 = s[c:d+1]
	# for x in range (c, d+1):
	# 	s2 = s2 + s[x]

	print (s1, s2)

if __name__ == "__main__":
  main()