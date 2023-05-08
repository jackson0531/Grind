# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# given a root, return true if it is a valid bst
# if min<curr.val<max
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root: Optional[TreeNode], minNum: int, maxNum: int) -> bool: 
        if not root: 
            return True
        if root.val<=minNum or root.val>=maxNum: 
            return False
        value = self.helper(root.left, minNum, root.val) and self.helper(root.right, root.val, maxNum)
        return value
