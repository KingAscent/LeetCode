class Solution {
    public int bitwiseComplement(int n) {
        int complement = 1;

        while(complement < n)
            complement = complement * 2 + 1;
        
        return complement - n;
    }
}
