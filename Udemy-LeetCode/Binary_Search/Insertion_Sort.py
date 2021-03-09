
###########
# SORTING #
###########

## Insertion Sort ##
def insertion_sort(A):
    # Create a new variable to store a copy of the list
    args = A
    # Iterate throught the list (i) times, beginning at 1 (to account for index offset) and ending at the list length.
    for i in range(1, len(args)):
        j = i-1
        # In each iteration, compare j with j+1 and back up through the entire list
        while args[j] > args[j+1] and j >= 0:
            args[j], args[j+1] = args[j+1], args[j]
            # Back us up through the list and compare until we're out @ -1
            j -= 1

    return args
