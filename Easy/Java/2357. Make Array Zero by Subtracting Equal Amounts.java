class Solution {
    public int minimumOperations(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int i : nums){
            if(0 < i)
                set.add(i);
        }

        return set.size();
    }
}
