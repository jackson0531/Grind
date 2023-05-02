# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# at each level we are comparing curr.val to max from the root
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        def dfs(root: TreeNode, maxNum: int): 
            nonlocal result
            if not root: 
                return 
            if root.val>=maxNum: 
                result+=1
                maxNum = root.val
            dfs(root.left, maxNum)
            dfs(root.right, maxNum)
        result = 0
        dfs(root, root.val)
        return result
