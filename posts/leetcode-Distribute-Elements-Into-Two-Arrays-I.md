# [LeetCode] Distribute Elements Into Two Arrays I (Python 풀이)

## 문제접근
https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

이 문제는 1-indexed 배열 nums의 원소들을 두 개의 배열 arr1, arr2에 나눠 담는 문제다.

첫 번째 원소는 arr1에, 두 번째 원소는 arr2에 넣고, 그 이후부터는 arr1의 마지막 원소와 arr2의 마지막 원소를 비교해서 arr1의 마지막 원소가 더 크면 arr1에, 그렇지 않으면 arr2에 넣는 규칙이다.

이 규칙을 그대로 따라가면서 두 배열을 채운 뒤 마지막에 이어 붙이면 result가 나온다는 점에 착안해, 배열 2개를 만들고 각각 초기화한 다음 세 번째 값부터 비교하며 넣어주고 마지막에 합치는 방식으로 접근했다.

## 풀이

**1.** arr1은 nums[0]으로, arr2는 nums[1]으로 각각 초기화한다.

**2.** nums의 세 번째 값(인덱스 2)부터 끝까지 순회하면서, arr1의 마지막 원소가 arr2의 마지막 원소보다 크면 arr1에, 그렇지 않으면 arr2에 현재 값을 추가한다.

**3.** 순회가 끝나면 arr1과 arr2를 이어 붙여 반환한다.

## 전체코드
```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # 배열 2개를 만들고 각각 초기화를 시켜준다.
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        # nums 세번째 값부터 비교를 하면서 넣어준다.
        for i in range(2, len(nums)):
            if (arr1[-1] > arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        # 마지막에 합친다.
        return arr1+arr2
```

\#배열 \#시뮬레이션
