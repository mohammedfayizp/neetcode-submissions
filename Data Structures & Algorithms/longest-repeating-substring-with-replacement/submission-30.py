class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        dic[s[0]]=1
        most_common=1
        left, right=0,0
        wrong=0
        final=1
        while(right<len(s)-1):
            right+=1
            dic[s[right]]+=1
            most_common=max(most_common, dic[s[right]])
            replacement=right-left+1-most_common
            while(right-left+1-most_common>k):  
                dic[s[left]]-=1
                left+=1
            final=max(final, right-left+1)
        return final
            




        