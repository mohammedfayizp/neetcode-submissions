class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right=0, len(heights)-1
        m=(len(heights)-1)*min(heights[0], heights[len(heights)-1])
        while(left<right):
            if(heights[left]<=heights[right]):
                left+=1
            elif(heights[left]>=heights[right]):
                right-=1
            m=max(m,(right-left)*min(heights[left], heights[right]))
        return m

            
        