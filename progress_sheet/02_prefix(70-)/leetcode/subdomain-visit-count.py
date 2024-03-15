class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for i in cpdomains:
            i=i.split()
            nu=int(i[0])
            we=i[1]
            we=we.split('.')
            for j in range(len(we)):
                si='.'.join(we[j:len(we)])
                dic[si]=dic.get(si,0)+nu
        li=[]
        for k,v in dic.items():
            li.append(str(v)+' '+k)
        return li