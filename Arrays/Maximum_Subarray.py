def maxSubArray(self, nums: List[int]) -> int:
    max = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max

def main():
    maxSubArray()

if __name__ == "__main__":
    main()