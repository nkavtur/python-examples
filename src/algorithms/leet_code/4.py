import statistics


class Solution:

    def find_smallest_k(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


sol = Solution()

# assert sol.find_smallest_k([0], [1, 2, 3, 4]) == 2

# assert sol.find_smallest_k([4], [1, 2, 3]) == 2.5

assert sol.find_smallest_k([1, 2], [3, 4]) == 2.5
assert sol.find_smallest_k([3, 4], [1, 2]) == 2.5
assert sol.find_smallest_k([1, 3], [2]) == 2
assert sol.find_smallest_k([], [1]) == 1
assert sol.find_smallest_k([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]) == 0
assert sol.find_smallest_k([1, 2], [-1, 3]) == 1.5
assert sol.find_smallest_k([1, 2, 3], [1, 2]) == 2

assert sol.find_smallest_k([1], [2, 3, 4]) == 2.5
assert sol.find_smallest_k([2], [1, 3, 4]) == 2.5

assert sol.find_smallest_k([3, 4], [1, 2]) == 2.5
assert sol.find_smallest_k([1, 7], [3, 4]) == 3.5

assert sol.find_smallest_k([3], [-2, -1]) == -1

assert sol.find_smallest_k([1], [2, 3, 4, 5]) == 3
#
