from Insertion_Sort import insertion_sort

testList = [12, 4, 67, 32, 3, 1]


#############
# SEARCHING #
#############

# Binary Search only works on sorted data set
sortedList = insertion_sort(testList)
print('Sorted list = ', sortedList)

## BINARY SEARCH ##


def binary_search(arr, target):
    # Define pointers:
    left = 0  # At the beginning of the list
    right = len(arr) - 1  # and at the end of the list

    # While the left pointer is less than the right pointer...
    while(left <= right):

        mid = (left+right)//2  # Find the middle and create a pointer

        # If the middle element between the left and right pointers is the target...
        if(arr[mid] == target):
            return mid           # Return the index

        elif(arr[mid] < target):  # Else if the middle is less than the target, the target is to the right
            left = mid+1         # Move the left pointer up to the middle + 1

        else:                    # Else the target is on the left of the mid
            right = mid-1        # and we should move the right pointer to the middle - 1

    return -1


print(binary_search(sortedList, 67))
