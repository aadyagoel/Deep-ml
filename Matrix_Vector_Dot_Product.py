def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	mat_r = len(a)
	mat_c = len(a[0])
	vec_r = len(b)
	c = [0]*mat_r
	if mat_c != vec_r:
		return -1
	else:
		for n in range(mat_r):
			for m in range(mat_c):
				c[n] += a[n][m]*b[m]
	return c
