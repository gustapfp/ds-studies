def twoSumBruteForce(nums: list[int], target: int) -> list[int]:
    high: int = 1
    low: int = 0
    while low < len(nums) - 1:
        while high < len(nums):
            sum = nums[high] + nums[low]
   
            if sum == target:
                print([low, high])
                return [low, high]
            high += 1
        low += 1
        high = low + 1

    print([-1, -1])
    return [-1, -1]

def twoSum(nums: list[int], target: int) -> list[int]:
    complements:dict[int, int] = {}
    for idx, number in enumerate(nums):
        complement: int = target - number
        if complements.get(number) is not None:
            return [complements.get(number, 1), idx]        
        complements[complement] = idx

    return [-1, -1]



if __name__ == "__main__":
    a_array =  [2,7,11,15]
    b_array = [3,2,4]
    c_array = [3,3]
    # twoSumBruteForce(
    #     nums=a_array,
    #     target=9
    # )
    # twoSumBruteForce(
    #     nums=b_array,
    #     target=6
    # )
    # twoSumBruteForce(
    #     nums=c_array,
    #     target=6
    # )
    print( twoSum(
        nums=a_array,
        target=9
    ))
    print(twoSum(
        nums=b_array,
        target=6
    ))
    print(twoSum(
        nums=c_array,
        target=6
    ))