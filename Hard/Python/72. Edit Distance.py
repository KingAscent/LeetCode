class Solution(object):
    def minDistance(self, word1, word2):
        # Create a two dimensional list of size (len(word1) + 1) * (len(word2) + 1)
        len1 = len(word1)
        len2 = len(word2)
        md = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Initialize the first row and column of the list with the corresponding indices
        for i in range(len1 + 1):
            md[i][0] = i
        for i in range(len2 + 1):
            md[0][i] = i

        # For each [i, j] calculate the minimum edit distance
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]: # Same characters
                    md[i][j] = md[i - 1][j - 1]
                else:
                    #          Deletion      Insertion
                    temp = min(md[i - 1][j], md[i][j - 1])
                    # Substituion
                    md[i][j] = min(md[i - 1][j - 1], temp) + 1
        
        # Return md[len1][len2] containing the minimum edit distance between
        # word1 and word2
        return md[len1][len2]
