class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> list = new ArrayList();

        for(int i = left; i <= right; i++){
            int number = i;
            while(0 < number){
                if((number % 10) != 0 && i % (number % 10) == 0)
                    number /= 10;
                else
                    number = -1;
            }
            if(number != -1)
                list.add(i);
        }

        return list;
    }
}
