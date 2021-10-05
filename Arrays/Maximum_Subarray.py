from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        copy = []
        for num in nums:
            copy.append(num)
        # Handles the case that all numbers are negative
        copy.sort()
        print(copy)
        if copy[len(copy) - 1] <= 0:
            return copy[len(copy) - 1]

        # Handles at least one non-negative number
        sum = 0
        max = nums[0]
        for num in nums:
            sum += num
            if sum < 0:
                sum = 0
            elif sum > max:
                max = sum

        return max




def main():
    test = [-2,1,-3,4,-1,2,1,-5,4]
    test2 = [1]
    test3 = [5,4,-1,7,8]
    test4 = [-2,1]
    test5 = [-2,-1, 0]
    print("The max sum is", Solution().maxSubArray(test))
    print("The max sum is", Solution().maxSubArray(test2))
    print("The max sum is", Solution().maxSubArray(test3))
    print("The max sum is", Solution().maxSubArray(test4))
    print("The max sum is", Solution().maxSubArray(test5))

if __name__ == "__main__":
    main()