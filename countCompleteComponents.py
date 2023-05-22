# given an int n, and undirected graph, return the number of complete connected componets of the graph
# connected components = Union Find
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1]*n

        def find(x) -> int:
            if parent[x]!=x: 
                parent[x] = parent[parent[x]]
                return find(parent[x])
            return x

        def union(x, y): 
            xParent = find(x)
            yParent = find(y)
            if xParent == yParent: 
                return 
            if size[xParent] > size[yParent]: 
                parent[yParent] = xParent
                size[xParent] += size[yParent]
            else: 
                parent[xParent] = yParent
                size[yParent] += size[xParent]

        freq = [0]*n
        for x,y in edges: 
            union(x, y)
            freq[x]+=1
            freq[y]+=1
        groups = set(find(i) for i in range(n))
        for i in range(n): 
            p = find(i)
            if freq[i]!=(size[p]-1): 
                groups.discard(p)
        return len(groups)
