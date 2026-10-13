class Solution(object):
    def isValid(self, s):
        stack=[]
        for n in s:
            if n in '({[':
                stack.append(n)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if n==')' and top!='(':
                    return False
                if n=='}' and top!='{':
                    return False
                if n==']' and top!='[':
                    return False
        return not stack
                 
        