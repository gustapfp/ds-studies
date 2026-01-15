def quicksort(array: list):
    if len(array) <= 1:
        return array

    pivot = array[0]
    less_than_pivot = [x for x in array[1:] if x <= pivot]
    greater_than_pivot = [x for x in array[1:] if x >= pivot]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


if __name__ == "__main__":
    list_data = [10, 20, 30, 20, 10, 40]
    print(quicksort(list_data))
    list1 = [15, 3, 42, 8, 23, 91, 7, 56]
    print(quicksort(list1))
    list2 = [100, -5, 42, -89, 0, 67, -23, 18]
    print(quicksort(list2))
    list3 = [3.14, 9.8, 1.5, 22.7, 0.5, 15.3, 8.1]
    print(quicksort(list3))
    list4 = [4, 6, 8.1, 10.1, 10.7]
    print(quicksort(list4))
