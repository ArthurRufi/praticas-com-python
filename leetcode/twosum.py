aba = []
def twoSum(self, nums, target):
        numbers = nums
        nlen = len(numbers)
        for x in range(nlen):
            for i in range (x + 1, nlen):
                if numbers[x] + numbers[i] == target:
                    aba = [x, i]