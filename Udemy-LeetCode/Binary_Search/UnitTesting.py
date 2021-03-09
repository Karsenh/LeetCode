from Insertion_Sort import insertion_sort

testList = [2, 24, 12, 125, 44]

testSort = insertion_sort(testList)
print(testSort)


def test_list_is_sorted():
    sortedList = insertion_sort(testSort)
    assert sortedList == testSort
