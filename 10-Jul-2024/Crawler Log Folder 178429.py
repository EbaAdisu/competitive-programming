# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for cmd in logs:
            if cmd == '../':
                count = max(count - 1, 0)
            elif cmd == './':
                pass
            else:
                count += 1
        return count

        