# Prompt: Conditions and Loops
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

def main():
	a, b = 4376, 8490
	sum = 0
	for x in range (a, b):
		if (x%2==1):
			sum = sum + x
	print (sum)


if __name__ == "__main__":
  main()