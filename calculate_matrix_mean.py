def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    r = len(matrix)
    c = len(matrix[0])
    
    if mode == 'row':
        means = [0]*r
        for n in range(r):
            for m in range(c):
                means[n] += matrix[n][m]
            means[n] = means[n]/r

    if mode == 'column':
        means = [0]*c
        for m in range(c):
            for n in range(r):
                means[m] += matrix[n][m]
            means[m] = means[m]/c
	return means
