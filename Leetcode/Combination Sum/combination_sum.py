class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target == 0: return [[]]
        result = []

        for num in candidates:
            remainder = target - num
            if remainder < 0: continue
            outputs = self.combinationSum(candidates, remainder)
            res = list(map(lambda way: [num, *way], outputs))
            result.extend(res)

        result = list(set(tuple(sorted(item)) for item in result))
        return result