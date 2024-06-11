# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        counter = Counter(arr1)
        real_pos = [0]*1001
        for num in arr1:
            if num not in arr2_set:
                real_pos[num] += 1

        arr2_ind = 0
        for ind in range(len(arr1)):
            arr1[ind] = arr2[arr2_ind]
            counter[arr2[arr2_ind]] -= 1
            if counter[arr2[arr2_ind]] == 0:
                arr2_ind += 1
            if arr2_ind == len(arr2):
                break
        print(arr1, ind)
        real_pos_pointer = 0

        for ind in range(ind + 1, len(arr1)):
            while real_pos_pointer < 1001 and real_pos[real_pos_pointer] == 0:
                real_pos_pointer += 1
            arr1[ind] = real_pos_pointer
            # print(arr1, ind, real_pos_pointer)
            real_pos[real_pos_pointer] -= 1
        return arr1
        