# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def zigzagLevelOrder(root,depth,ans):
            if root:
                if len(ans) < depth+1:
                    ans.append(deque())
                if depth%2:
                    ans[depth].appendleft(root.val)
                else:
                    ans[depth].append(root.val)
                zigzagLevelOrder(root.left,depth + 1,ans)
                zigzagLevelOrder(root.right,depth + 1,ans)
            return ans
        return zigzagLevelOrder(root,0,[])
