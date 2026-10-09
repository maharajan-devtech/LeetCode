class Solution(object):
    def groupAnagrams(self, strs):
        group=defaultdict(list)
        for n in strs:
            key="".join(sorted(n))
            group[key].append(n)
        return list(group.values())
        