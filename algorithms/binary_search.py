def binary_serch(array: list[int], target: int ) -> int:
    """Binary Search Algorithm usign two pointers, high and low, to store the indexes.

    - Temporal Complexity: O(logN)
    - Memory Complexity: O(1) -> Will always store the same spaces (mid, high, and low)
    - Leet code link: https://leetcode.com/submissions/detail/1827347426/
    Args:
        array (list[int]): list of sorted interger
        target (int): the desired number

    Returns:
        int: The index from the target or -1 if not found
    """
    high: int = len(array)
    low: int = 0
    steps = 0
    while high > low:
        steps += 1 
        mid: int = int((high + low)/2)
        print(f"mid value: {mid}")
        
        if array[mid] == target:
            print(f"Total Steps for an array with {len(array)} elements: {steps}")
            return mid
        elif target > array[mid]: 
            low = mid +1
        else: 
            high = mid
    return -1

array_a = [1, 4, 9, 16, 25]
array_b = [2, 3, 4, 5, 7, 11, 13, 17]
array_c = [0, 4, 6, 12, 18, 24, 30, 36, 42, 48]
array_d = [-10, -3, 0, 2, 4, 8, 15, 23, 42, 56, 78]

if __name__ == "__main__":
    target = 4
    result = binary_serch(array_a, target)
    print(f"Array A Result:{result}")
    result = binary_serch(array_b, target)
    print(f"Array B Result:{result}")
    result = binary_serch(array_c, target)
    print(f"Array C Result:{result}")
    result = binary_serch(array_d, target)
    print(f"Array D Result:{result}")
