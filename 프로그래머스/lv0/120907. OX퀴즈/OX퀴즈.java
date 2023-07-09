import java.util.*;
class Solution {
    public String[] solution(String[] quiz) {
        String[] arr = {};
        List<String> list = new ArrayList<>(Arrays.asList(arr));
        
        for (int i=0; i<quiz.length; i++) {
            String[] str = quiz[i].split(" ");
            
            int x = Integer.parseInt(str[0]);
            int y = Integer.parseInt(str[2]);
            int z = Integer.parseInt(str[4]);
            
            int result = 0;
            
            if (str[1].equals("+")) {
                result = x+y;
            } else {
                result = x-y;
            }
            
            if (result == z) {
                list.add("O");
            } else {
                list.add("X");
            }
        }
        String[] answer = list.toArray(new String[list.size()]);
        return answer;
    }
}