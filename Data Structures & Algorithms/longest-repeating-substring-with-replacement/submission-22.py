class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        dic[s[0]]=1
        most_common=s[0]
        left, right=0,0
        wrong=0
        final=1
        while(right<len(s)-1):
            right+=1
            dic[s[right]]+=1
            if(dic[s[right]]>dic[most_common]):
                most_common=s[right]
            replacement=right-left+1-dic[most_common]
            if(replacement>k):   
                dic[s[left]]-=1
                left+=1
                continue
            else:
                final=max(final, right-left+1)
        return final
            




        