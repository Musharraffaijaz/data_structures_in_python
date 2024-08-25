#InsertionSort
def insertionSort(number_list):
    for i in range(1, len(number_list)):
        keyElement = number_list[i]
        j = i - 1
        while j >=0 and keyElement < number_list[j]:
            number_list[j+1] = number_list[j]
            j -= 1
        number_list[j + 1] = keyElement

if __name__ == "__main__":
    number_list = [12, 11, 13, 5, 6]
    insertionSort(number_list)
    print("Sorted array is:", number_list)