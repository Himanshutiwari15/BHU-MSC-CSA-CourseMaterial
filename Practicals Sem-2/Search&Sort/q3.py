# https://www.youtube.com/watch?v=w4W6yya1PIc

def maxSubArray(nums):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here += nums[i]
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# nums = [-2, -3, 4, -1, -2, 1, 5, -3]
nums = [1,5,3,-2,4]
print("Maximum contiguous sum is", maxSubArray(nums))
