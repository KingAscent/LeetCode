class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int fs = 0;
        int ts = 0;
        int ansKey = 0;
        int start = 0;
        int end = 0;

        while(end < answerKey.length()){
            if(answerKey.charAt(end) == 'F')
                fs++;
            else
                ts++;
            while(k < Math.min(fs, ts)){
                if(answerKey.charAt(start) == 'F')
                    fs--;
                else
                    ts--;
                start++;
            }
            ansKey = Math.max(ansKey, fs + ts);
            end++;
        }

        return ansKey;
    }
}
