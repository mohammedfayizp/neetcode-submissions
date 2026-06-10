class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        temp1, temp2= Counter(s), Counter(t)
        if(temp1==temp2):
            return True
        else:
            return False
        