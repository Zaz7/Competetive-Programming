class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack= [ ]
        last_to_first = { ")" : "(","]" : "[","}" : "{"}
        for l in s:
            if l in last_to_first:
                if stack and stack[-1] == last_to_first[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return True if not stack else False
