# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True
        if root is None:
            return True

        def dfs(root: Optional[TreeNode]):

            if root is None:
                return 0

            leftHeight = dfs(root.left) 
            rightHeight = dfs(root.right)

            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False

            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return self.balanced    
