class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] arr = new int[n];
        
        // 학생들 기본값 초기화
        for (int i=0; i<n; i++) {
            arr[i] = 1;
        }
        // 여벌옷 가지고 온 학생
        for (int r : reserve) {
            arr[r-1] += 1;
        }
        // 잃어버린 학생
        for (int l : lost) {
            arr[l-1] -= 1;
        }
        // 여벌옷 나누기
        for (int i=0; i<n; i++) {
            if (arr[i] == 0) {
                if (i-1 >= 0 && arr[i-1] == 2) {
                    arr[i] += 1;
                    arr[i-1] -= 1;
                } else if (i+1 < n && arr[i+1] == 2) {
                    arr[i] += 1;
                    arr[i+1] -= 1;
                }
            }
        }
        // 참여 학생들 세기
        for (int a : arr) {
            if (a >= 1) {
                answer++;
            }
        }
        
        return answer;
    }
}

// 최대한 많은 학생이 수업을 들어야함 -> 그리디, 최적의 조합을 찾자.
// 여벌옷이 있다면 총 2벌이 있는 것임 -> 한명한테밖에 못빌려줌

// 접근 방법 1
// reserve를 순회하면서 번호를 확인한다.
// lost에 reserve 번호가 없다면, 해당 번호-1, 해당번호+1 두 값이 lost에 있는지, arr에 값이 있는지 확인한 후 있는 값중에 작은 값을 arr배열에 추가 및 answer +2
// lost에 reserve 번호가 있다면, 그냥 answer 1을 더함.
// -> reserve를 순회하면서 풀면 너무 복잡할 것 같다.

// 접근 방법 2
// 번호가 오름차순 번호기 때문에 배열을 활용해서 각 자리마다 옷을 몇벌 가지고 있는 지 체크
// 기본 1벌씩 가지고 있다고 하고 초기화
// reserve 배열 순회 -> +1
// lost 배열 순회 -> -1
// arr에서 0인 애를 만났을때 본인의 앞 뒤가 있다면 +1 및 해당 원소 -1 아니면 패스
// arr에서 0이 아닌 수를 세면 정답