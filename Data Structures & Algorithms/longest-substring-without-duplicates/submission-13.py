class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data_pos=defaultdict(int)
        left, right=0,-1
        final=0
        start=0
        for i in range(len(s)):
            if((s[i] not in data_pos) or (data_pos[s[i]]<left)):
                data_pos[s[i]]=i
            else:
                left=data_pos[s[i]]+1
                data_pos[s[i]]=i   
            final=max(final, i-left+1)
        return final
                
            
            

        