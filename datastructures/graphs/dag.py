from collections import defaultdict


class DAG:
    def __init__(self, vertices=None, edges=None):
        self._vertices = []
        self._edges = defaultdict(list)

        if vertices:
            for v in vertices:
                self.add_vertex(v)

        if edges:
            for from_, to in edges:
                self.add_edge(from_, to)

    def add_vertex(self, value):
        if value not in self._vertices:
            self._vertices.append(value)

    def add_edge(self, from_, to):
        if to not in self._edges[from_]:
            self._edges[from_].append(to)

    def bfs(self, from_, to):
        """
        procedure BFS(G, root) is
            let Q be a queue
            label root as discovered
            Q.enqueue(root)
            while Q is not empty do
                v := Q.dequeue()
                if v is the goal then
                    return v
                for all edges from v to w in G.adjacentEdges(v) do
                    if w is not labeled as discovered then
                        label w as discovered
                        Q.enqueue(w)
        """

    def dfs(self, from_, to):
        """
        procedure DFS_iterative(G, v) is
            let S be a stack
            S.push(v)
            while S is not empty do
                v = S.pop()
                if v is not labeled as discovered then
                    label v as discovered
                    for all edges from v to w in G.adjacentEdges(v) do
                        S.push(w)
        """

    def __repr__(self):
        return f"{dict(self._edges)}"
