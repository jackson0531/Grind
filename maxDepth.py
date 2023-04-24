# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# given root, return max depth, start with 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion DFS
        #if not root:
        #    return 0
        #return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        # Iteration BFS
        if not root:
            return 0
        queue = [root]
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result+=1
        return result
