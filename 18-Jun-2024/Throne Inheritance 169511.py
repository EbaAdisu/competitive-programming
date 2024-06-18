# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.root = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(name):
            if name not in self.dead:
                ans.append(name)
            for new_name in self.graph[name]:
                dfs(new_name)
            return ans
        return dfs(self.root)

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()