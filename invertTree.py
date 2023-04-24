class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ''' Recursion DFS
        if root==None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''
        # Iteration BFS with queue
        if not root: 
            return root
        queue = [root] 
        while queue:
            size = len(queue)
            for i in range(size): 
                curr = queue.pop(0)
                curr.left, curr.right = curr.right, curr.left
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root 
