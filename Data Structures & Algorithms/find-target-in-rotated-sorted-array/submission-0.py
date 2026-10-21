class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        def binary_search(low, high) -> int:
            while low <= high:
                mid = low + (high-low) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1 

        # find pivot
        # choose a midpoint, if mid > high, pivot is in right half. if mid < high, left half
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # perform binary search on left half and right half
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
