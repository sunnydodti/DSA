def lengthOfLongestSubstring(s: str):
    start: int = 0
    length: int = 0
    map: dict[str, int] = {}

    print(s)
    for i in range(len(s)):
        print(f"i:{i}:{s[i]}")
        if s[i] in map:
            print(f"i:{s[i]} exists at {map[s[i]]}")

            print(f"deleting {start}-{map[s[i]]}")
            new_start = map[s[i]] + 1
            for j in range(start, map[s[i]]+1):
                print(f"\t deleting {s[j]} at {j}")
                del map[s[j]]
            start = new_start
            print(f"{start=} {length=}")

        map[s[i]] = i
        print(
            f"length: {length} or i({i})-start({start})+1 : {i - start + 1} = {max(length, i - start + 1)}")
        length = max(length, i - start + 1)
        print(f"{map=} {length=}")

    return length


if __name__ == '__main__':
    print(lengthOfLongestSubstring('zara'))
    print(lengthOfLongestSubstring('zarafatima'))
    print(lengthOfLongestSubstring('zaraqureshi'))
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('bbbbb'))
    # print(lengthOfLongestSubstring('pwwkew'))
    # print(lengthOfLongestSubstring('dvdf'))
    # print(lengthOfLongestSubstring('aaa'))
