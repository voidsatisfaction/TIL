class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i, j = 0, 0
        state_set = set()
        max_count = 0

        while True:
            while s[j] not in state_set:
                state_set.add(s[j])
                max_count = max(max_count, j-i+1)
                j += 1
                
                if j == len(s):
                    return max_count

            while s[j] in state_set:
                state_set.remove(s[i])
                i += 1

# more optimized

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i, j = 0, 0
        index_dict = {}
        max_count = 0

        while True:
            while (s[j] not in index_dict) or (index_dict[s[j]] < i):
                index_dict[s[j]] = j
                max_count = max(max_count, j-i+1)
                j += 1
                
                if j == len(s):
                    return max_count

            i = index_dict[s[j]]+1

if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3