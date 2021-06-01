from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []

        #setup dictionary
        letters = dict()
        nums = [3] * 8; nums[5]+=1; nums[7]+=1
        current = ord('a')
        for i in range(2,10):
            letters[i] = []
            for j in range(0,nums[i-2]):
                letters[i].append(chr(current)); current += 1
                
        #recursive call
        combos = []
        self.getCombos(letters, '', combos, digits)
        return combos

    def getCombos(self, letters, current, combos, digits):
        if(len(current)==len(digits)): combos.append(current); return
        for character in letters[int(digits[len(current)])]:
            self.getCombos(letters, current+character, combos, digits)

s = Solution()
print(s.letterCombinations('23'))