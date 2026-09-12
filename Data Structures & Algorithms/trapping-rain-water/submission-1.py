class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax= [0] * len(height)
        rightmax=[0] * len(height)
        left=0
        right=0
        minlr=[0] * len(height)
        water=0
        for i in range(len(height)):
            leftmax[i]=left
            if(left<height[i]):
                left=height[i]
        for i in range(len(height)-1,0,-1):
            rightmax[i]=right
            if(right<height[i]):
                right=height[i]
        for j in range(len(leftmax)):
            minlr[j]= min(leftmax[j],rightmax[j])
        
        for i in range(len(height)):
            if((minlr[i]-height[i])>0):
                water=water+minlr[i]-height[i]
        return water


