class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1 =0
        left =0
        right = len(heights)-1

        while(left<right):
            h = min(heights[left],heights[right])
            width=right-left
            amt=h*width
            max1= max(max1,amt)

            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1        

        return max1
