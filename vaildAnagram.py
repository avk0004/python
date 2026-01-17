class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        44 casse passed remain 10 cased
        """
        m1 = list(s)
        n1 = list(t)
        l = set(m1)
        ll = set(n1)
        return l.issuperset(ll) and ll.issuperset(l)
M = Solution()
X= M.isAnagram("rat","car")
print(X)