class Solution:
    def sortSentence(self, s: str) -> str:
        count = 0

        for char in s:
            if char == ' ':
                count += 1

        sentence = [""] * (count + 1)

        i, j = 0, 0

        while j < len(s):
            try:
                if int(s[j]):
                    sentence[int(s[j]) - 1] = s[i: j]
                    j += 2
                    i = j
            except:
                j += 1

        return " ".join(sentence)


s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))
print(s.sortSentence("Myself2 Me1 I4 and3"))
