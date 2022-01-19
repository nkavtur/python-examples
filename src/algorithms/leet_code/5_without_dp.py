class Solution:
    def longestPalindrome(self, s: str):
        if s == s[::-1]:
            return s

        longest_start_index, longest_end_index = 0, 0
        for i in range(0, len(s) - 1):
            low, high = -1, len(s) + 1

            # even case
            if s[i] == s[i + 1]:
                low, high = i, i + 1
                while high < len(s) and s[i] == s[high]:
                    high += 1
                high -= 1

            # odd case
            elif s[i - 1] == s[i + 1]:
                low, high = i - 1, i + 1

            while low >= 0 and high < len(s) and s[low] == s[high]:
                (longest_start_index, longest_end_index) = (longest_start_index, longest_end_index) \
                    if (longest_end_index - longest_start_index + 1) > (high - low + 1) \
                    else (low, high)
                low -= 1
                high += 1

        return s[longest_start_index:longest_end_index + 1]

