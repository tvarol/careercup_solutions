#Numbers with 4 are considered to be unlucky, floor numbers are skipped with numbers with 4; for a top level n, ask how many layers there are actually;
#for example n=20, that is 18 levels [Remove 4, 14]                                                                                                         

class Solution:
    def find_levels(self,n):
        a = n//10
        rem = n%10
        if rem > 5:
            return n - (a+1)
        else:
            return n-a

        #return (n-((n-4)//10+1))
        
mySol = Solution()
print(mySol.find_levels(20))
