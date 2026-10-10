class Solution(object):
    def minRotations(self, n, s):
        def rotation(a,b):
            diff=abs(a-b)
            return min(diff,10-diff)
        total=0
        curr=0
        for ch in s:
            digit=int(ch)
            total+=rotation(curr,digit)
            curr=digit
        ans=total
        for i in range(n):
            
            prev=0 if i==0 else int(s[i-1])
            first=int(s[i])
            last=int(s[-1])

            old=rotation(prev,first)
            new=rotation(prev,last)
            cand=total-old+new
            ans=min(ans,cand)
        return ans
            
            
        