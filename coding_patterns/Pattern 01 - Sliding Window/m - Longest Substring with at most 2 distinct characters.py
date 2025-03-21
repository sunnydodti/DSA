def lengthOfLongestSubstringTwoDistinct(s: str):
    start = 0
    length = 0
    map: dict[str, int] = {}

    print(s)
    for end in range(len(s)):
        if s[end] not in map:
            map[s[end]] = 0
        map[s[end]] += 1
        print(f"{map=}")

        while len(map) > 2:
            map[s[start]] -= 1
            if (map[s[start]] == 0):
                del map[s[start]]
                print(f"\td-{map=}")
            start += 1
        length = max(length, end - start + 1)

    return length


if __name__ == '__main__':
    print(lengthOfLongestSubstringTwoDistinct('zaaaraa'))
    print(lengthOfLongestSubstringTwoDistinct('zara'))
    print(lengthOfLongestSubstringTwoDistinct('eceba'))
    print(lengthOfLongestSubstringTwoDistinct('ccaabbb'))
    print(lengthOfLongestSubstringTwoDistinct('z'))
