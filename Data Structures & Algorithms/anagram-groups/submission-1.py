class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            dic[frozenset(Counter(list(i)).items())].append(i)
        l=[]
        for i in dic:
            l.append(dic[i])
        return l

        