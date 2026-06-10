class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                m=max(m, (j-i)*min(heights[i],heights[j]))
        return m

        