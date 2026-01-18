class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        Time Complexity = O(1)
        Space Complexity= O(1)

        """
        M =0
        if x>0:
            M =1
            M = int(x**.5)

        return M
N=int(input())       
M= Solution()
X = M.mySqrt(N)
print(X)
