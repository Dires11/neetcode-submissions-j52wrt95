class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", '/'}
        for op in range(len(tokens)):
            if tokens[op] in operands:
                num2 = stack.pop()
                num1 = stack.pop()
                print(num1, tokens[op], num2, end=' =' )
                match tokens[op]:
                    case "+":
                        num1 += num2
                    case "-":
                        num1 -= num2
                    case '*':
                        num1 *= num2
                    case "/":
                        num1 = int(num1 / num2)
                print(num1)
                stack.append(num1)
            else:
               stack.append(int(tokens[op]))
        print(stack)
        return stack[-1]

