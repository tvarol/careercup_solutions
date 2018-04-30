#Given two sets of intervals such as {[1, 2], [4, 8]} and {[2, 5]}. Find their union {[1, 8]} for the two intervals.

class Solution:
    def find_union(self,nums1,nums2):
        interval1 = []
        #if isinstance(nums1[0], list): 
        for i in range(len(nums1)):
           interval1.extend(range(nums1[i][0],nums1[i][1]+1))  
    
        for j in range(len(nums2)):
            interval1.extend(range(nums2[j][0],nums2[j][1]+1))

        interval1 = list(set(interval1))

        union = []
        start = interval1[0]
        for i in range(1,len(interval1)):   
            if interval1[i]!=interval1[-1] and interval1[i] - interval1[i-1] == 1: continue
            else:
                if interval1[i]==interval1[-1]:
                    end = interval1[i]
                else:
                    end = interval1[i-1]
                union.append([start, end])
                start = interval1[i]
            
        return union


nums1 = [[1,2],[7,8]] 
nums2 = [[2,5]]      

mySol = Solution()
print(mySol.find_union(nums1,nums2))
