def unique_pairs(nums, target):
    seen = set()
    pairs = set()
    
    for num in nums:
        rem = target - num
        if rem in seen:
            temp=[num,rem]
            temp.sort()
            pairs.add(tuple(temp))
            
        seen.add(num)
    
    return list(pairs)

# Example usage
nums = [2, 4, 3, 6, 7, 1, 5]
target = 8
print(unique_pairs(nums, target))