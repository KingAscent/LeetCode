class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>();

        for(int i = 0; i <= rowIndex; i++){
            row.add(1);
            for(int j = i - 1; 0 < j; j--){
                row.set(j, row.get(j - 1) + row.get(j));
            }
        }

        return row;
    }
}
