class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos={order[i]:i for i in range(26)}
        # print(pos)
        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                # print(j,pos[words[i][j]],pos[words[i+1][j]])
                if pos[words[i][j]] <pos[words[i+1][j]]:
                    break
                elif pos[words[i][j]] >pos[words[i+1][j]]:
                    return False
            else:
                if len(words[i])>len(words[i+1]):
                    return False
        return True

        