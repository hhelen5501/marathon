import unittest
from pprint import pprint
from typing import List


class Solution:

    def __init__(self):
        self.beautiful = 0

    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        self.beautiful = 0

        sets = []
        self.generate(nums, k, [], 0, sets)
        return self.beautiful

    def generate(
            self,
            array: List[int],
            k: int,
            current: List[int],
            minimum_index: int,
            sets: List[List[int]]
    ):
        if len(current) != 0:
            if self.is_beautiful(current, k):
                self.beautiful += 1
                sets.append(current)
            else:
                # If this is not beautiful none of its super-arrays will be beautiful
                return

        for i in range(minimum_index, len(array)):
            self.generate(
                array,
                k,
                current + [array[i]],
                i + 1,
                sets
            )

    def is_beautiful(self, array: List[int], k: int) -> bool:
        if len(array) == 1:
            return True

        for i in range(len(array) - 1):
            if abs(array[i] - array[-1]) == k:
                return False

        return True


if __name__ == '__main__':
    sets = []
    Solution().generate([4, 2, 5, 9, 10, 3], 1, [], 0, sets)
    pprint(sets)
