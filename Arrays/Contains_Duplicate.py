def containsDuplicate(self, nums: List[int]) -> bool:
    s = set()
    for num in nums:
        if s.__contains__(num):
            return True
        else:
            s.add(num)
    return False

def main():
    containsDuplicate()

if __name__ == "__main__":
    main()