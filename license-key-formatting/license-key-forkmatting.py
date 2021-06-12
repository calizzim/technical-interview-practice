class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        s = s.upper()
        start = len(s) % k
        ans = s[0:start]
        for index in range(start,len(s)):
            if len(ans) and (index-start)%k == 0:
                ans += '-'
            ans += s[index]
        return ans

s = Solution()
print(s.licenseKeyFormatting('he-llo123',3))