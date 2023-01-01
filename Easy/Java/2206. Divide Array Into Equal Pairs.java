class Solution {
    public boolean divideArray(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for(int i : nums){
            if(seen.contains(i))
                seen.remove(i);
            else
                seen.add(i);
        }

        return seen.size() == 0;
    }
}
