nums = [1, 1, 2, 1, 3, 2, 3, 2]
    
major1 = major2 = nums[0]
count1 = count2 = 0
    
# 对抗阶段
for each in nums:
    if major1 == each:
        count1 += 1
        continue
    
    if major2 == each:
        count2 += 1
        continue
    
    if count1 == 0:
        major1 = each
        count1 = 1
        continue
    
    if count2 == 0:
        major2 = each
        count2 = 1
        continue
    
    count1 -= 1
    count2 -= 1
    
# 统计阶段
if nums.count(major1) > len(nums) / 3:
    print(f"主要元素1: {major1}")
if nums.count(major2) > len(nums) / 3:
    print(f"主要元素2：{major2}")