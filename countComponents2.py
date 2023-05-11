# given int n and an ajencency list, undirected graph; return the num of connected components 
# an edge represents connectivity 
# dfs and mark everything as seen
# first store every node
# Union Find 
# implement union combine two trees
# implement find find the parent
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)] # each element is their own parent
        size = [1] * n # the tree size of each element as the node
        def find(element: int) -> int: 
            if parent[element]==element: 
                return element
            else: 
                return find(parent[element])

        def union(x: int, y: int) -> int:
            xParent = find(x)
            yParent = find(y)
            if xParent==yParent: 
                return 0
            else: 
                if size[xParent]>=size[yParent]: 
                    parent[yParent] = xParent
                    size[xParent]+=size[yParent]
                else: 
                    parent[xParent] = yParent
                    size[yParent]+=size[xParent]
                return 1

        reuslt = n
        for edge in edges: 
            reuslt -= union(edge[0], edge[1])
        return reuslt
