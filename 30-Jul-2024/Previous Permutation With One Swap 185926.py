# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        small_ind = N-1
        stack = []
        for ind in range(N-1,-1,-1):
            if not stack or stack[-1][0] > arr[ind]:
                stack.append((arr[ind], ind))
            elif stack[-1][0] == arr[ind]:
                stack.pop()
                stack.append((arr[ind], ind))
            
            else:
                poped = ind
                while stack and stack[-1][0] < arr[ind]:
                    poped = stack.pop()[1]
                # print(poped, ind)
                arr[ind],arr[poped] = arr[poped], arr[ind]
                # arr[ind+1:] = sorted(arr[ind+1:])
                return arr
            # print(stack,arr[ind], ind)
        return arr
        