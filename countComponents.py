# given int n and an ajencency list, undirected graph; return the num of connected components 
# an edge represents connectivity 
# dfs and mark everything as seen
# first store every node
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dict = collections.defaultdict(list)
        for edge in edges: 
            dict[edge[0]].append(edge[1])
            dict[edge[1]].append(edge[0])
        seen = set()
        result = 0
        def dfs(node: int): 
            for neighbor in dict[node]: 
                if neighbor not in seen: 
                    seen.add(neighbor)
                    dfs(neighbor)
        for edge in edges: 
            if edge[0] not in seen: 
                dfs(edge[0])
                result += 1
        return result + n-len(seen)
