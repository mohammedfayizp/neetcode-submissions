class Solution:

    def encode(self, strs: List[str]) -> str:
        ls=[len(i) for i in strs]
        temp=''
        if(len(strs)//10==0):
            temp+='00'+str(len(strs))
        elif(len(strs)//100==0):
            temp+='0'+str(len(strs))
        else:
            temp+=str(len(strs))
        for i in range(len(ls)):
            if ls[i]//10 ==0:
                ls[i]='00'+str(ls[i])
            elif ls[i]//100 ==0:
                ls[i]='0'+str(ls[i])
            else:
                ls[i]=str(ls[i])
            temp+=ls[i]
        for i in strs:
            temp+=i
        return temp
        

    def decode(self, s: str) -> List[str]:
        l=int(s[:3])
        il=[]
        last=0
        for i in range(l):
            il.append(int(s[3+3*i:6+3*i]))
            last=i
        s=s[6+3*last:]
        final=[]
        for i in range(l):
            temp=s[:il[i]]
            final.append(temp)
            s=s[il[i]:]
        return final

