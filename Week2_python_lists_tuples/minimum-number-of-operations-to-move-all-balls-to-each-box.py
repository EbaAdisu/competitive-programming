class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        pre=[]
        pos=[]
        cl=pl =l =cr=pr=r=0
        for i in range(n):
            #print(pl,l )
            pre+=[pl+l]
            if boxes[i]=="1":
                cl+=1
                pl+=cl +l
                l=0
            else:
                #l=cl 
                pl+=l
                l=cl 
            pos+=[r+pr]
            if boxes[-i-1]=="1":
                cr+=1
                pr+=cr+r
                r=0
            else:
                pr+=r
                r=cr
        print(pre,pos[::-1] )
        pos=pos[::-1]
        ans=[]
        for i in range(n):
            ans+=[pos[i]+pre[i]]
        return ans 
            