def longestSubstringWithKdistinct(s: str, k: int):
    start: int = 0
    max_l: int = 0
    map = {}

    for end in range(len(s)):
        if s[end] not in map:
            map[s[end]] = 0
        map[s[end]] += 1

        while len(map) > k:
            map[s[start]] -= 1
            if map[s[start]] == 0:
                del map[s[start]]
            start += 1
        max_l = max(max_l, end-start+1)

    return max_l


if __name__ == '__main__':
    print(longestSubstringWithKdistinct("araaci", 2))
