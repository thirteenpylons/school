def main(rows, columns):
	for i in range(rows):
		for j in range(columns):
			if i % 2 == 0:
				print("*", end="")
			else:
				if j == 0 or j == columns - 1:
					print("*", end="")
				else:
					print(" ", end="")
		print()