def find_nearest_neighbors(numbers):
    result = []
    nums = list(numbers)
    
    for i in range(len(nums)):
        current = nums[i]
        min_diff = float('inf')
        best_neighbor = None
        
        for j in range(len(nums)):
            if i == j:
                continue
            diff = abs(current - nums[j])
            if diff < min_diff or (diff == min_diff and nums[j] < best_neighbor):
                min_diff = diff
                best_neighbor = nums[j]
        
        result.append(best_neighbor)
    
    return result

if __name__ == "__main__":
    input_numbers = [-5, 1, 12, 17, 0, 13, 8, 3, 8]
    output = find_nearest_neighbors(input_numbers)

    print("Input:", input_numbers)
    print("Output:", output)