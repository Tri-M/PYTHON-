def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  aveg = (total-high-low) / (items-2)
  return aveg