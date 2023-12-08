class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        direc=defaultdict(list)
        for p in paths:
            s=p.split()
            path=s[0]
            for i in range(1,len(s)):
                f=s[i].split('(')
                direc[f[1][:-1]]+=[path+'/'+f[0]]
        return list(v for v in  direc.values() if len(v)>1)
        