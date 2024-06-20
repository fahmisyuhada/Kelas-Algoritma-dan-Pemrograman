



def selection_sort(array):
    n = len(array)

    for i in range(0,n-1): 
        min_index = i # asumsi nilai minimum awal
        
        for j in range(i+1,n):
            if array[min_index] > array[j]: # jika benar nilai minimum baru ditemukan
                min_index = j
        
        if(min_index != i):
            # swap
            tmp = array[i]
            array[i] = array[min_index] 
            array[min_index] = tmp
    
    return array

# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array

data = [7, 12, 9, 11, 3]


sort_list = insertionSort(data)
print(sort_list)
