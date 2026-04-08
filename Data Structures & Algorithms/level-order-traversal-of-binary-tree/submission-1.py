# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals = {}

        def dfs(root, depth):
            if not root:
                return
            if depth in vals.keys():
                vals[depth].append(root.val)
            else:
                vals[depth] = [root.val]
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        res = []
        for i in vals.keys():
            res.append(vals[i])
        print(vals)
        

        return res