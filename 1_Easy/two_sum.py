testList = [3, 3]
target = 6

def twoSum(list, target):

    solution = []

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] + list[j] == target):
                solution.append(i)
                solution.append(j)

                return solution

print(twoSum(testList, target))
