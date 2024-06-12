# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        NAMELENGTH =  len(name)
        TYPEDLENGTH =  len(typed)
        name_pointer = 0
        typed_pointer = 0
        while name_pointer < NAMELENGTH and typed_pointer < TYPEDLENGTH:
            if name[name_pointer] == typed[typed_pointer]:
                name_pointer += 1
                typed_pointer += 1
            elif name_pointer > 0 and typed[typed_pointer] == name[name_pointer - 1]:
                typed_pointer += 1
            else:
                return False
        while typed_pointer < TYPEDLENGTH:
            if name_pointer > 0 and typed[typed_pointer] == name[name_pointer - 1]:
                typed_pointer += 1
            else:
                return False
        return name_pointer == NAMELENGTH