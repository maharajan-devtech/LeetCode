class Solution(object):
    def minRotations(self, s):
        current=0
        total=0
        for ch in s:
            target=int(ch)
            distance=abs(current-target)
            rotation=min(distance,10-distance)
            total+=rotation
            current=target
        return total
        