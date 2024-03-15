class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        if 1> len(nums) == 2:
            GesamtSumme = sum(nums)
            return GesamtSumme
        else:
            m = len(nums) // 2
            ArrayErsten = nums[:m]
            ArrayLetzten = nums[m:]
            SummeErsten = 0
            SummeLetzten = 0  # Füge die Deklaration der Variable SummeLetzten hinzu

        # Zähle die Anzahl der Einsen in der ersten Hälfte
            for i in ArrayErsten:
                SummeErsten += i

        # Zähle die Anzahl der Einsen in der zweiten Hälfte
            for i in ArrayLetzten:
                SummeLetzten += i

            if SummeErsten >= SummeLetzten:
                return SummeErsten
            else:
                return SummeLetzten


solution = Solution()
nums = [1, 1]
print(solution.findMaxConsecutiveOnes(nums))



# nums = [1, 1, 0, 1, 1, 1]
# nums = [1, 0, 1, 1, 0, 1]
# print(findMaxConsecutiveOnes(nums))
