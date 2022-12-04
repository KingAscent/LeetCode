class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> fb = new ArrayList<String>();

        for(int i = 1; i <= n; i++){
            if(i % 15 == 0)
                fb.add("FizzBuzz");
            else if(i % 3 == 0)
                fb.add("Fizz");
            else if(i % 5 == 0)
                fb.add("Buzz");
            else
                fb.add(Integer.toString(i));
        }

        return fb;
    }
}
