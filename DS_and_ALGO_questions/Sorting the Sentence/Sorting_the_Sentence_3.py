class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        final_word_list = [""] * len(word_list)

        for word in word_list:
            final_word_list[int(word[-1]) - 1] = word[: -1]

        return " ".join(final_word_list)


s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))
print(s.sortSentence("Myself2 Me1 I4 and3"))
