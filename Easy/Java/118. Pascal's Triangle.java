class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pas = new ArrayList<>();

        for(int i = 0; i < numRows; i++){
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for(int j = 1; j < i; j++){
                row.add(pas.get(i - 1).get(j - 1) + pas.get(i - 1).get(j));
            }
            if(0 < i)
                row.add(1);
            pas.add(row);
        }

        return pas;
    }
}
