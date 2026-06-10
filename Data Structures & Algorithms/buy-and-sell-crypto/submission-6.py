class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right=0, len(prices)-1
        for i in range(len(prices)-1):
            if(left<right):
                if(prices[i+1]<prices[left]):
                    if(i+1<right):
                        left=i+1
                if(prices[len(prices)-2-i]>prices[right]):
                    if(len(prices)-2-i>left):
                        right=len(prices)-2-i
            else:
                break
        return max(0,prices[right]-prices[left])
        