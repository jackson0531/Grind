class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(root) -> bool: 
            nonlocal count
            # base case 
            if not root: 
                return True
            left, right = True, True
            if root.left: 
                left = helper(root.left) and (root.val==root.left.val)
            if root.right: 
                right = helper(root.right) and (root.val==root.right.val)
            if left and right: 
                count+=1
                return True
            else: 
                return False
        count = 0
        helper(root)
        return count
