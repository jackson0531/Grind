# given a string s, partition the string so that each letter appears only in one partition
# find the range of each letter in the str and update the right pointer 
# if new_letter appears within prev one's, we have to include it
# map store the last apearance position of a letter
class Solution:
    def partitionLabels(self, s: str) -> List[int]: 
        myMap = collections.defaultdict(int)
        for index, l in enumerate(s): 
            myMap[l] = index
        result = []
        left, right = 0, -1
        for index, l in enumerate(s):
            if myMap[l]>right: 
                right = myMap[l]
            if index==right: 
                result.append(right-left+1)
                left = right+1   
        return result
