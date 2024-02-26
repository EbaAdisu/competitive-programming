# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column = defaultdict(list)
        def verTrav(root,depth,col):
            nonlocal column
            if root:
                column[col].append((root.val,depth))
                verTrav(root.left,depth+1,col-1)
                verTrav(root.right,depth+1,col+1)
            return 
        verTrav(root,0,0)
        answer = []
        for key in sorted(column):
            column[key].sort(key = lambda x: (x[1],x[0]))
            chachi = []
            for e,d in column[key]:
                chachi.append(e)
            answer.append(chachi)
        return answer
        