class Solution:
    def trap(self, height: List[int]) -> int:
        Lmax= 0
        
        total=0
        for i in range(len(height)-1):
            Rmax = 0
            if height[i]>Lmax:
                Lmax =height[i]
            for j in range(i,len(height)):
                if height[j]>=Lmax:
                    Rmax = height[j]
                    break
                
                elif height[j]>Rmax:
                    Rmax = height[j]

            total+= min(Lmax,Rmax) - height[i]

        return total


                




        