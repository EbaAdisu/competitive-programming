class Solution:
    def simplifyPath(self, path: str) -> str:
        pathes = path.split('/')
        stack = []
        for path in pathes:
            if path == '.' or not path: continue
            if path == '..':
                if stack:
                    stack.pop()
            else:
                stack += [path]
        return '/' + '/'.join(stack)        