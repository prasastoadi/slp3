def edit_distance_matrix(source, target, cost=[1,1,2]):
    """
    Parameters:
        source: Source string.
        target: Target string.
        cost: List of insertion, deletion, and substitution costs.

    Returns:
        Edit distance matrix.
    """
    s_len = len(source)
    t_len = len(target)
    distance = [[i for i in range(t_len+1)] for i in range(s_len+1)]

    for i in range(t_len+1):
        distance[0][i] = i
    for i in range(s_len+1):
        distance[i][0] = i

    for i in range(1, s_len+1):
        for j in range(1, t_len+1):
            distance[i][j] = min(distance[i][j-1]+cost[0],
                    distance[i-1][j]+cost[1],
                    distance[i-1][j-1]+cost[2]*(source[i-1] != target[j-1]))
    return distance

def min_edit_distance(source, target, cost=[1,1,2]):
    """
    Parameters:
        source: Source string.
        target: Target string.
        cost: List of insertion, deletion, and substitution costs.

    Returns:
        Minimum edit distance.
    """
    distance = edit_distance_matrix(source, target, cost)[-1][-1]
    return distance
