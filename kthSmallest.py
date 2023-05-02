# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# in order traversal 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        def dfs(root: Optional[TreeNode], k: int): 
            nonlocal count, result
            if not root: 
                return 
            dfs(root.left, k)
            count+=1
            if (count==k): 
                result = root.val
                return
            dfs(root.right, k)
        count, result = 0, 0
        dfs(root, k)
        return result
