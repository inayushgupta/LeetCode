# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS SOLUTION

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def dfs(node, depth):
            nonlocal res
            if not node:
                return
            
            if len(res) == depth:
                res.append(node.val)
            else:
                res[depth] = node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)          

        dfs(root, 0)
        return res

# BFS SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                rightside = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(rightside.val)

        return res
