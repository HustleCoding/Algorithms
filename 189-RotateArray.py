class Solution:
    def reversed_numbers(self, arr: List[int], left: int, right: int) -> None:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        self.reversed_numbers(nums, 0, len(nums) - 1)
        self.reversed_numbers(nums, 0, k - 1)
        self.reversed_numbers(nums, k, len(nums) - 1)