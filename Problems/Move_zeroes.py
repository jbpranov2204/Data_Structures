def Movezeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

nums = [0, 1, 0, 3, 12]
Movezeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
