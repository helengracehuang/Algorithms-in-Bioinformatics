# Prompt: Variables and Some Arithmetic
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

def main():
	a = 977
	b = 975
	c = a*a+b*b
	print ("The square of the hypotenuse of the right triangle is", c)

if __name__ == "__main__":
  main()