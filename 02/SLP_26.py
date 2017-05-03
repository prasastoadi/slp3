def edit_distance(source, target, cost=[1,1,2]):
    """
    Parameters:
        source : Source string
        target : Target string
        cost : List of insertion, deletion, and substitution costs
    """
    s_len = len(source)
    t_len = len(target)

    D = [[i for i in range(t_len+1)] for i in range(s_len+1)]

    for i in range(t_len+1):
        D[0][i] = i
    for i in range(s_len+1):
        D[i][0] = i

    for i in range(1, s_len+1):
        for j in range(1, t_len+1):
            D[i][j] = min(D[i][j-1]+cost[0],
                          D[i-1][j]+cost[1],
                          D[i-1][j-1]+cost[2]*(source[i-1] != target[j-1]))
    return D
