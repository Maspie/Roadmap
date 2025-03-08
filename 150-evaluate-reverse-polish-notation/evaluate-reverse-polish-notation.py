class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for c in tokens:

            if c == "+":
                new = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(new)
                print("add", new)
            elif c == "*":
                new = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(new)
                print("mul", new)
            elif c == "/":
                new = stack[-2] // stack[-1] if stack[-2] * stack[-1] >= 0 else -(-stack[-2] // stack[-1])

                stack.pop()
                stack.pop()
                stack.append(new)
                print("div", new)
            elif c == "-":
                new = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(new)
                print("sub", new)
            else:
                stack.append(int(c))
        
        return stack[-1]


