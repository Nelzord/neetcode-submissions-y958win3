# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkSubtree(root, minVal, maxVal):
            if not root:
                return True

            elif minVal < root.val < maxVal:
                return checkSubtree(root.left, minVal, root.val) and checkSubtree(root.right, root.val, maxVal)
            else:
                return False

        return checkSubtree(root, float("-inf"), float("inf"))
