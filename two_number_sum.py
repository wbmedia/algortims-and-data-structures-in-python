array = [3, 5, -4, 8, 11, 1, -1, 6]


# target sum 10
# current number x
# x + y = 10 sum of two numbers in array list
# y = 10 - x
# y = 10 - 3 = 7

# O(n^2) time | O (1) space
def two_number_sum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

    return []


print(two_number_sum([11-1], 10))


# O(n) time | O(n) space
def towNumbersSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch - num, num]
        else:
            nums[num] = True
    return []


print(towNumbersSum([11-1], 10))


# O(nlog(n)) time | O(1) space
def TowNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left]], array[right]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []


print(TowNumberSum([11-1], 10))