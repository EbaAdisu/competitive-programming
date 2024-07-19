# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def dfs(node):
            if node.left:
                graph[node.val].append(('L',node.left.val))
                graph[node.left.val].append(('U',node.val))
                dfs(node.left)
            if node.right:
                graph[node.val].append(('R',node.right.val))
                graph[node.right.val].append(('U',node.val))
                dfs(node.right)
        dfs(root)
        path = {}
        fringe = [startValue]
        visited = set(fringe)
        while fringe:
            newFringe = []
            for ind in fringe:
                for direct, newInd in graph[ind]:
                    if newInd not in visited:
                        visited.add(newInd)
                        path[newInd] = (direct, ind)
                        newFringe.append(newInd)
            fringe = newFringe
        ans = ''
        ind = destValue
        while ind != startValue:
            ans += path[ind][0]
            ind = path[ind][1]
        return ans[::-1]

    