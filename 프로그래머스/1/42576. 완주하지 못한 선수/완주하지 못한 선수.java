import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> raceMap = new HashMap<>();
        
        // 1. 참여자 명단을 Map에 카운팅 (getOrDefault 활용)
        for (String part : participant) {
            raceMap.put(part, raceMap.getOrDefault(part, 0) + 1);
        }
        
        // 2. 완주자 명단을 돌며 카운트 차감 (-1)
        for (String comp : completion) {
            raceMap.put(comp, raceMap.getOrDefault(comp, 0) - 1);
        }
        
        // 3. 카운트가 0이 아닌 사람(완주하지 못한 선수) 찾기
        for (String key : raceMap.keySet()) {
            if (raceMap.get(key) != 0) {
                answer = key;
            }
        }
        
        return answer;
    }
}

// Q. 해시에서 집합을 이용하는 거를 이용해보면 되지 않을까?
// 동명이인 때문에 해시맵을 이용하자.
// Q. 비교를 어떻게 할 수 있을까
// 1. 참여자, 완주자 해시 맵을 만든다.
// 2. 참여자 배열을 순회해서 양쪽 해시맵에 원소가 있는 지 없는 지 파악
// -> 양쪽에 다 없는 경우 얘가 정답
// -> 중복 케이스는 양쪽 value 값이 다른 경우 얘가 정답
// -> 위 방법은 공간복잡도 면에서 효율이 안좋을 듯하다.
// 1. 참여자를 기준으로 해시맵을 만들어서 value를 이름 수로 한다.
// 2. 완주자 배열을 순회하면서 참여자 해시맵 value를 차감한다.
// -> value가 0이 아닌 친구가 완주 못한 애