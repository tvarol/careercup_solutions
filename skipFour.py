#Numbers with 4 are considered to be unlucky, floor numbers are skipped with numbers with 4; for a top level n, ask how many layers there are actually; for example n=20, that is 18 levels [Remove 4, 14]


class Solution:
    def find_levels(self,n):
        nums = str(list(range(1,n+1)))
        print(type(nums))
        print(nums)
        count=0
        for idx,val in enumerate(nums):
            if "4" in nums[idx]: 
                count += 1

        return (n - count)

mySol = Solution()
print(mySol.find_levels(25))
        
        

