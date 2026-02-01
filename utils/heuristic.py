#Check manhattan distance
def heuristic(A, Z):
    return abs(A[0] - Z[0]) + abs(A[1] - Z[1])