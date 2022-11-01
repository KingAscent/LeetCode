class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Filter out arrays of length 1
        if(strs.length == 1)
            return strs[0];
              
        String prefix = strs[0];
        
        // Go over each string in the array, checking if
        // the prefix appears at the start of the string,
        // and if so, continuously keep track of the largest
        for(int i = 1; i < strs.length; i++){
            while(strs[i].indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() - 1);
            }
        }
        
        return prefix;
    }
}
