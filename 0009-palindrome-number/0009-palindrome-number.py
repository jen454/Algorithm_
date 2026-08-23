class Solution:
    def isPalindrome(self, x: int) -> bool:
        begin = 0
        end = len(str(x))-1

        while (begin <= end):
            if (str(x)[begin] != str(x)[end]):
                return False
            begin += 1
            end -= 1
        
        return True

# 투포인터 사용해보자.
# 양쪽 값이 다르면 false