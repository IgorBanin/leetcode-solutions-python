def removeDuplicates(self, nums: List[int]) -> int:
    if(len(nums) == 0):
        return 0
    currNum = nums[0]
    counter = 1
    for num in nums:
        if num != currNum:
            nums[counter] = num
            currNum = num
            counter += 1
    return counter

def main():
    removeDuplicates()

if __name__ == "__main__":
    main()