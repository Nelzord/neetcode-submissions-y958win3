# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.solution = {}

        self.dfs(root, 0)
        print(self.solution)

        res = []
        for i in self.solution.keys():
            res.append(self.solution[i][0])
        return res

    def dfs(self, root, h):
        if not root:
            return
        if h in self.solution.keys():
            self.solution[h].append(root.val)
        else:
            self.solution[h] = [root.val]
        
        self.dfs(root.right, h + 1)
        self.dfs(root.left, h + 1)
        