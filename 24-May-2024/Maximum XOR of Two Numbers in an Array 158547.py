# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = defaultdict(int)
        def insert(trie, num: int) -> None:
            cur = trie
            for i in range(31, -1,-1):
                bit = 0
                if  num & 1<<i:
                    bit = 1
                if bit not in cur:
                    cur[bit] = defaultdict(int)
                cur = cur[bit]
        def search_max_hamming(trie, num):
            cur = trie
            new_num = 0
            bi = ''
            for i in range(31, -1,-1):
                bit = 0
                if  num & 1<<i:
                    bit = 1

                if 1-bit in cur:
                    new_num <<= 1
                    new_num += (1-bit)
                    cur = cur[1-bit]
                else:
                    new_num <<= 1
                    new_num += (bit)
                    cur = cur[bit]
            return new_num ^ num

        for num in nums:
            insert(trie, num)
        answer = 0
        for num in nums:
            answer = max(answer, search_max_hamming(trie, num))
        return answer
