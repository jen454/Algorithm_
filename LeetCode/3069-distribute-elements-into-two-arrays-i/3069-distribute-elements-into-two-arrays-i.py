class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if (arr1[-1] > arr2[-1]):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2

# 배열 2개를 만들고 각각 초기화를 시켜준다.
# nums 세번째 값부터 비교를 하면서 넣어준다.
# 마지막에 합친다.