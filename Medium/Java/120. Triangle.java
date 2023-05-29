class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] path = new int[triangle.size() + 1];

        for(int i = triangle.size() - 1; 0 <= i; i--){
            for(int j = 0; j < triangle.get(i).size(); j++){
                path[j] = Math.min(path[j], path[j + 1]) + triangle.get(i).get(j);
            }
        }

        return path[0];
    }
}
