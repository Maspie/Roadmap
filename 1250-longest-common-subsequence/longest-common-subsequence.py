class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):

            for j in range(len(text2)-1, -1, -1):

                if text1[i] == text2[j]:
                    rows[i][j] = 1 + rows[i+1][j+1]

                else:
                    rows[i][j] = max(rows[i+1][j], rows[i][j+1])


        return rows[0][0]
        