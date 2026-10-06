class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right = len(s1)
        b= Counter(s1)
        while(right<=len(s2)):
            if(b== Counter(s2[left:right])):
                return True
            left+=1
            right+=1
        
        return False