class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # classic palindrome problem: go thru array, expand from middle (n^2)
        # so we can recurse - for each palindrome we see, we recurse on the remainder of the string
        # optimization: i feel like with different combination, sometimes we'll revisit the same "remainder of the string", so if we can store all different combinations and make different combinations with these, it'd cut down runtime, sacrificing space
        # res = []
        # currList = []
        
        # def backtrack(start): # start denotes where substring of s starts
        #     def isPalindrome(s):
        #         i = 0
        #         j = len(s) - 1
        #         while i <= j:
        #             if s[i] != s[j]:
        #                 return False
        #             i += 1
        #             j -= 1
        #         return True

        #     if start >= len(s):
        #         res.append(currList[:])
        #         return

        #     for i in range(start, len(s)):
        #         if isPalindrome(s[start : i+1]):
        #             currList.append(s[start : i+1])
        #             backtrack(i + 1)
        #             currList.pop()
        # backtrack(0)
        # return res

        # dp preprocessing - expand from middle (should be O(n^2))
        dp = set()
        for i in range(len(s)):
            p1 = p2 = i
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                dp.add((p1, p2))
                p1 -= 1
                p2 += 1
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                dp.add((p1, p2))
                p1 -= 1
                p2 += 1
                
        res = []
        currList = []

        def backtrack(start):
            if start >= len(s):
                res.append(currList[:])
                return

            for i in range(start, len(s)):
                if (start, i) in dp:
                    currList.append(s[start : i+1])
                    backtrack(i + 1)
                    currList.pop()
        backtrack(0)
        return res



