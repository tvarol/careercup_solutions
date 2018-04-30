#Find the length of the non repeated numbers in an array. 
#Input : 1,2,2,3,4,5,6,2,3

class Solution(object):
    def find_length(self,nums):
        return len(set(nums))

myList = [1,2,2,3,4,5,6,2,3]
mySolution = Solution()
print(mySolution.find_length(myList))

