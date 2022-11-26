class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> set = new HashSet<>();
        sentence = sentence.replaceAll("[^a-zA-Z]", "");

        for(int i = 0; i < sentence.length(); i++){
            if(!set.contains(sentence.charAt(i)))
                set.add(sentence.charAt(i));
        }

        return set.size() == 26;
    }
}
