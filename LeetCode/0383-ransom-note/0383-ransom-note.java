class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        boolean answer = true;
        char[] ransomArr = ransomNote.toCharArray();
        char[] magazineArr = magazine.toCharArray();

        HashMap<Character, Integer> ransomMap = new HashMap<>();

        for (char note : ransomArr) {
            ransomMap.put(note, ransomMap.getOrDefault(note, 0) + 1);
        }

        for (char maga : magazineArr) {
            ransomMap.put(maga, ransomMap.getOrDefault(maga, 0) + -1);
        }

        for (char key : ransomMap.keySet()) {
            if (ransomMap.get(key) > 0) {
                answer = false;
            }
        }
        
        return answer;
    }
}