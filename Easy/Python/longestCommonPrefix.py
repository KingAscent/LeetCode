class Solution(object):
    def longestCommonPrefix(self, strs):
        # Filter strings of length 1
        if(len(strs) == 1):
            return strs[0]
        
        prefix = strs[0]
        
        # Go over each string in the array, checking if
        # the prefix appears at the start of the string,
        # and if so, continuously keep track of the largest
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if len(j) <= i or j[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]
