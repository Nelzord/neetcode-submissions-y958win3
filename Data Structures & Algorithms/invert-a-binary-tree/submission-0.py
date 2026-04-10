# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if not root:
                return
            else:
                left = root.right
                right = root.left

                root.left = left
                root.right = right

                invert(root.left)
                invert(root.right)
            return 

        invert(root)
        return root