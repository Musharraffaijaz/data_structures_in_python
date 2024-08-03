def binarySearch(number_list, number_to_search):
    start = 0
    end = len(number_list) - 1
    while start <= end:
        mid = (start + end)//2
        if number_list[mid] < number_to_search:
            start = mid + 1
        elif number_list[mid] > number_to_search:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    number_list = [1,2,3,4,5,6,7,8,9]
    number_to_search = 5
    index = binarySearch(number_list, number_to_search)
    print(f"The index of {number_to_search} is at {index} index")