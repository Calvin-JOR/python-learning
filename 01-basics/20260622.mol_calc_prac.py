nums = [1, 1, 2, 1, 3, 2, 3, 2]
m1 = m2 = nums[0]
count1 = count2 = 0

for each in nums:
    if m1 == each:
        count1 += 1
        continue
    if m2 == each:
        count2 += 1
        continue
    if count1 == 0:
        m1 = each
        continue
    if count2 == 0:
        m2 = each
        continue
    count1 -= 1
    count2 -= 1

if nums.count(m1) > len(nums)/3:
    print(m1)
if nums.count(m2) > len(nums)/3:
    print(m2)