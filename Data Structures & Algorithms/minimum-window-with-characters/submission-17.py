class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t=Counter(t)
        left, right=0,0
        real={}
        for i in s:
            if i in t:
                if i not in real:
                    real[i]=1
                else:
                    real[i]+=1
        for i in t:
            if i not in s:
                real[i]=0
        for i in real:
            if(real[i]<t[i]):
                return ''
        for i in range(len(s)):
            if(s[i] not in t):
                left+=1
            else:
                break
        right=left
        for i in t:
            real[i]=0
        current_dic=set()
        short=s
        while(right<len(s)):
            if(s[right] in t):
                real[s[right]]+=1
                if(real[s[right]]==t[s[right]]):
                    current_dic.add(s[right])
            if(len(current_dic)==len(t)):
                if(s[left] in t):
                    while(real[s[left]]>t[s[left]]):
                        real[s[left]]-=1
                        left+=1
                        while(s[left] not in t):
                            left+=1
                short=short if len(short)<(right-left+1) else s[left:right+1]
            right+=1
        return short
                    

            

                






                
                    





        