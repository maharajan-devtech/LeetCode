class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for n in s:
            count[n]=1+count.get(n,0)
        for n in t:
            if n not in count:
                return False
            count[n]-=1
            if count[n]<0:
                return False
        return True      