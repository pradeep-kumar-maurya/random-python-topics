class Solution:
    def sortSentence(self, s: str) -> str:
        count = 0

        for char in s:
            if char == ' ':
                count += 1

        sentence = [""] * (count + 1)

        i = 0
        ans = ""

        while i < len(s):
            try:
                if int(s[i]):
                    sentence[int(s[i]) - 1] = ans
                    i += 2
                    ans = ""
            except:
                ans += s[i]
                i += 1

        return " ".join(sentence)


s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))
print(s.sortSentence("Myself2 Me1 I4 and3"))
