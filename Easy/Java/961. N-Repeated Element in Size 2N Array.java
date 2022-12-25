class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer, Integer> appearance = new HashMap();
        int num = 0;

        for(int i : nums){
            if(appearance.containsKey(i))
                appearance.put(i, appearance.get(i) + 1);
            else
                appearance.put(i, 1);
        }

        for(int i : nums){
            if(appearance.get(i) == (nums.length / 2)){
                num = i;
                break;
            }
        }

        return num;
    }
}
