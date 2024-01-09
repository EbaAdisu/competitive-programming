class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        f = 0
        s = 0

        while f < len(name) and s < len(typed):
            if name[f] == typed[s]:
                f += 1
                s += 1
            else:
                if f > 0 and typed[s] == name[f-1] :
                    s+=1
                else:
                    return False

        if f != len(name):
            return False
        while s < len(typed):
            if typed[s] == name[f-1] :
                    s+=1
            else:
                return False
        return True
