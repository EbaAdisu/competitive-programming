# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def give_it_paranthesis(root):
            if root:
                left = give_it_paranthesis(root.left)
                right = give_it_paranthesis(root.right)
                if not (left or right):
                    return f"{root.val}"
                elif right:
                    return f"{root.val}({left})({right})"
                return f"{root.val}({left})"
            return ''
            
        return give_it_paranthesis(root)
