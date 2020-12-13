
file_in = open('01.in', "r")
nums = [int(num) for num in file_in]
nums.sort()

def find(target, nums):
    le, ri = 0, len(nums) - 1
    
    while le < ri:
        current_sum = nums[le] + nums[ri]
        if current_sum < target:
            le += 1
        elif current_sum > target:
            ri -= 1
        else:
            break
    else:
        return None
    return nums[le], nums[ri]

def original():
    fi, sec = find(2020, nums)
    return fi * sec, (fi, sec)

def optional():
    for i, fi in enumerate(nums):
        result = find(2020 - fi, nums[:i] + nums[i+1 :])

        if result is not None:
            sec, thi = result[0], result[1]
            return fi * sec * thi, (fi, sec, thi)    
    
