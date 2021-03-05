
###########
# SORTING #
###########
## Insertion Sort ##
def insertion_sort(A):
    args = A
    for i in range(1, len(args)):
        j = i-1
        while args[j] > args[j+1] and j >= 0:
            args[j], args[j+1] = args[j+1], args[j]
            j -= 1

    return args
