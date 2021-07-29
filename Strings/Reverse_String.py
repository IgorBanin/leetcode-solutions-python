def reverseString(self, s: List[str]) -> None:
    end = len(s) - 1
    for i in range(len(s) // 2):
        temp = s[i]
        s[i] = s[end]
        s[end] = temp
        end -= 1

def main():
    reverseString()

if __name__ == "__main__":
    main()