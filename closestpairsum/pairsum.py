def closest_pair_sum(num_list, target):
    if len(num_list) < 2:
        return None
    nums = sorted(num_list)
    left = 0
    right = len(nums) - 1
    closest_pair = (nums[left], nums[right])
    closest_diff = abs(nums[left] + nums[right] - target)
    while left < right:
        current_sum = nums[left] + nums[right]
        current_diff = abs(current_sum - target)
        if (current_diff < closest_diff) or (current_diff == closest_diff and current_sum < sum(closest_pair)):
            closest_diff = current_diff
            closest_pair = (nums[left], nums[right])
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return (nums[left], nums[right])
    return closest_pair