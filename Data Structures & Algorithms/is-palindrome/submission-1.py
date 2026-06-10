class Solution:
    def isPalindrome(self, s: str) -> bool:
        re=''
        for i in s:
            if(ord(i)>=ord('0') and ord(i)<=ord('9')):
                re+=i
            elif(ord(i)>=ord('a') and ord(i)<=ord('z')):
                re+=i
            elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                re+=i.lower()
        for i in range(len(re)//2):
            if(re[i]!=re[-1-i]):
                return False
        return True

        