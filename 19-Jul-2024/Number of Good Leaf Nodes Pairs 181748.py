# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self,=0, left=None, right=None):
#         self =
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def n_distance(leaf_ind,d):
            ans = 0
            fringe = [leaf_ind]
            visited = set(fringe)
            while fringe and d:
                new_fringe = []
                for ind in fringe:
                    for new_ind in graph[ind]:
                        if new_ind not in visited:
                            if new_ind in leaf:
                                ans += 1
                            visited.add(new_ind)
                            new_fringe.append(new_ind)
                fringe = new_fringe                        
                d -= 1
            return ans
        graph = defaultdict(list)
        leaf = set()
        fringe = [root]
        while fringe:
            new_fringe = []
            for node in fringe:
                if node.left:
                    graph[node.left].append(node)
                    graph[node].append(node.left)
                    new_fringe.append(node.left)
                if node.right:
                    graph[node.right].append(node)
                    graph[node].append(node.right)
                    new_fringe.append(node.right)
                if not(node.left or node.right):
                    leaf.add(node)
            fringe = new_fringe
        # print(leaf)
        ans = 0
        for ind in leaf:
            ans += n_distance(ind,distance)
        # print(ans)
        return ans//2
        

        