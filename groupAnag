class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map1 = defaultdict(list)
        for st in strs:
            sort = "".join(sorted(st))
            map1[sort].append(st)
        
        return map1.values()
