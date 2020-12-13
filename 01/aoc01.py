
def main():
    file_in = open('01.in', "r")
    nums = [int(num) for num in file_in]
    nums.sort()
    le, ri = 0, len(nums) - 1
    
    while le < ri:
        current_sum = nums[le] + nums[ri]
        if current_sum < 2020:
            le += 1
        elif current_sum > 2020:
            ri -= 1
        else:
            break
    else:
        raise RuntimeError
    
    return nums[le] * nums[ri]

