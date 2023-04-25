# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]) -> int: 
            nonlocal res 
            if not node: 
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # update the result 
            res = max(res, left+right)
            return 1+max(left, right)
        
        res = 0
        depth(root)
        return res
