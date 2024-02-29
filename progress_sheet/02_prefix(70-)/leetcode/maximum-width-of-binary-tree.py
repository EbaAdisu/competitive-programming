# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def lst():
            return [float('inf'), float('-inf')]
        depth_width = defaultdict(lst)
        ans = 0
        def width(root,depth,column):
            nonlocal ans
            if root:
                depth_width[depth][0] = min(depth_width[depth][0], column)
                depth_width[depth][1] = max(depth_width[depth][1], column)
                if (depth_width[depth][0] <= 0 and depth_width[depth][1] <= 0)  or (depth_width[depth][0] > 0 and depth_width[depth][1] > 0):
                    ans = max(ans, depth_width[depth][1] - depth_width[depth][0] + 1)
                else:
                    ans = max(ans, depth_width[depth][1] - depth_width[depth][0])
                column*=2
                width(root.left,depth+1,column - 1 if column >= 0 else column)
                width(root.right,depth+1,column + 1 if column <= 0 else column)
            return ans
        return width(root,0,0)