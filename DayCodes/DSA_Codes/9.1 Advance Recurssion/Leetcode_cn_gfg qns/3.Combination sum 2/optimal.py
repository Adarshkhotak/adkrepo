from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(subset, index, target):
            if target == 0:
                result.append(subset.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue #go to nxt loop
                if candidates[i] > target:
                    break
                subset.append(candidates[i])
                backtrack(subset, i + 1, target - candidates[i])
                subset.pop()

        candidates.sort()  #first we need to sort
        result = []
        backtrack([], 0, target)
        return result