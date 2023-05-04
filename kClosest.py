# calculate the distance of each point to origin and sort it 
# 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        dist = [(index, math.sqrt(l[0]**2 + l[1]**2)) for index, l in enumerate(points)]
        #sorted(dist, key=lambda x:dist[1])
        dist.sort(key=lambda x:x[1])
        #kth = dist[k][1] # real kth closest distance
        result = [points[dist[i][0]] for i in range(k)]
        return result
        '''
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
