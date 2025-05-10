def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    r = len(a)
    c = len(a[0])
    b = [[0 for _ in range(r)] for _ in range(c)]
    for n in range(r):
        for m in range(c):
            b[m][n] = a[n][m]
	return b
