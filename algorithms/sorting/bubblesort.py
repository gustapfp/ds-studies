def bubblesort(array: list) -> list:
    for _ in array:
        array_size = len(array)
        is_sorted = True
        for i in range(array_size - 1):
            high = array[i + 1]
            low = array[i]

            if low > high:
                is_sorted = False
                array[i], array[i + 1] = high, low
        print(array)
        if is_sorted:
            print("-------------------------")
            return array
    print("-------------------------")
    return array


if __name__ == "__main__":
    list_data = [10, 20, 30, 20, 10, 40]
    bubblesort(list_data)
    list1 = [15, 3, 42, 8, 23, 91, 7, 56]
    bubblesort(list1)
    list2 = [100, -5, 42, -89, 0, 67, -23, 18]
    bubblesort(list2)
    list3 = [3.14, 9.8, 1.5, 22.7, 0.5, 15.3, 8.1]
    bubblesort(list3)
    list4 = [4, 6, 8.1, 10.1, 10.7]
    bubblesort(list4)
