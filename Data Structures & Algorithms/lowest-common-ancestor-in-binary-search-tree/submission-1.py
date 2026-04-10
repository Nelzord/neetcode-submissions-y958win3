# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = []
        lca = None
        ref = root
        while root:
            ancestors.append(root.val)
            if root.val == p.val:
                break
            elif root.val < p.val:
                root = root.right
            else:
                root = root.left
            
        while ref:
            
            if ref.val in ancestors:
                lca = ref

            if ref.val == q.val:
                break
            if ref.val < q.val:
                ref = ref.right
            else:
                ref = ref.left
        
        return lca