# 2.7 Augment the minimum edit distance algorithm to output an alignment;
# you will need to store pointers and add a stage to compute the backtrace.

class EditDistance:

    def __init__(self):
        self.source = None
        self.target = None
        self.cost = None
        self.distance_matrix = None
        self.pointer_matrix = None

    def fit(self, source, target, cost=[1,1,1]):
        self.source = source
        self.target = target
        self.cost = cost

        self._compute()

    def _compute(self):
        s_len = len(self.source)
        t_len = len(self.target)
        D = [[i for i in range(t_len+1)] for i in range(s_len+1)]
        pointer = [[i for i in range(t_len+1)] for i in range(s_len+1)]

        for j in range(t_len+1):
            D[0][j] = j
            pointer[0][j]=[(0, j-1, 'ins')]
        for i in range(s_len+1):
            D[i][0] = i
            pointer[i][0]=[(i-1, 0, 'de')]

        pointer[0][0] = [(0,0, 'null')]

        for i in range(1, s_len+1):
            for j in range(1, t_len+1):
                ins = D[i][j-1]+self.cost[0]
                de = D[i-1][j]+self.cost[1]
                sub = D[i-1][j-1]+self.cost[2]*(self.source[i-1] != self.target[j-1])

                mini = min(ins, de, sub)

                directions = [(i,j-1, 'ins')*(ins==mini),
                              (i-1,j, 'de')*(de==mini),
                              (i-1,j-1, 'sub')*(sub == mini)]
                pointer[i][j] = [x for x in directions if x]
                D[i][j] = mini
        self.distance_matrix = D
        self.pointer_matrix = pointer

    def minimum(self):
        return self.distance_matrix[-1][-1]

    def matrix(self):
        return self.distance_matrix

    def operation(self):

        s_len = len(self.source)
        t_len = len(self.target)
        ith = s_len
        jth = t_len
        ppath = []

        while ith > 0 or jth > 0:
            parent = self.pointer_matrix[ith][jth]
            ith_parent, jth_parent, action= parent[0]
            if action == 'ins':
                ppath.append((self.target[jth-1], 'ins'))
            elif action == 'de':
                ppath.append((self.source[ith-1], 'de'))
            elif action == 'sub':
                ppath.append((self.target[jth-1], 'sub'))

            ith, jth = ith_parent, jth_parent

        ppath.reverse()
        return ppath

    def step(self, short=True):
        path = self.operation()
        source = list(self.source)
        by_step = []
        idx = 0
        by_step.append(self.source)
        for p in path:
            if p[1] == 'ins':
                source.insert(idx, p[0])
                idx += 1
            elif p[1] == 'de':
                del source[idx]
            elif p[1] == 'sub':
                if short and source[idx] == p[0]:
                    idx +=1
                    continue
                source[idx] = p[0]
                idx += 1

            by_step.append(''.join(source))
        return by_step
