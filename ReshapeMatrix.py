import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    r1 = len(a)
    c1 = len(a[0])
    s1 = r1*c1

    r2 = new_shape[0]
    c2 = new_shape[1]
    s2 = r2*c2

    if s1!=s2:
        return []
    reshaped_matrix = [[0 for _ in range(c2)]for _ in range(r2)]
    temp = []


    for n in range(r1):
        for m in range(c1):
            temp.append(a[n][m])
    i = 0
    for n in range(r2):
        for m in range(c2):
            reshaped_matrix[n][m]=temp[i]
            i+=1
    return reshaped_matrix
