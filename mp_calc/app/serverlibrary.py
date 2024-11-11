import typing

def mergesort(array, byfunc=None):
  mergesort_recursive(array, 0, len(array)-1, byfunc)
  
# start_i = p
# end_i = r
# middle_i = q

def merge(array: list, p: int, q: int, r: int, byfunc=None) -> None:
    left_n = q-p + 1
    right_n = r-q
    leftarr = array[p:q+1]
    rightarr = array[q+1:r+1]
    left_pointer = 0
    right_pointer = 0
    destination = p     # starts of arr
    
    while left_pointer < left_n and right_pointer < right_n:
        left_value = byfunc(leftarr[left_pointer]) if byfunc else leftarr[left_pointer]
        right_value = byfunc(rightarr[right_pointer]) if byfunc else rightarr[right_pointer]
        
        if left_value < right_value:
            array[destination] = leftarr[left_pointer]
            left_pointer += 1
        else:
            array[destination] = rightarr[right_pointer]
            right_pointer += 1
        destination += 1
        
    while left_pointer < left_n:
        array[destination] = leftarr[left_pointer]
        left_pointer += 1
        destination += 1
    while right_pointer < right_n:
        array[destination] = rightarr[right_pointer]
        right_pointer += 1
        destination += 1   
        
def mergesort_recursive(array: list, p: int, r: int, byfunc) -> None:
    if r>p:
        q = (p+r)//2
        mergesort_recursive(array,p,q, byfunc)
        mergesort_recursive(array,q+1,r, byfunc)
        merge(array, p, q, r, byfunc)
        

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack. Raises an error if the stack is empty."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        """Return the item on the top of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


class EvaluateExpression:
    def __init__(self, expression):
        self.expression = expression

    def precedence(self, operator):
        """Return the precedence of the operator."""
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        return 0

    def apply_operator(self, operands, operator):
        """Apply the operator to the top two operands in the stack."""
        right = operands.pop()
        left = operands.pop()
        if operator == '+':
            operands.push(left + right)
        elif operator == '-':
            operands.push(left - right)
        elif operator == '*':
            operands.push(left * right)
        elif operator == '/':
            operands.push(left / right)

    def to_postfix(self):
        """Convert the infix expression to postfix notation."""
        output = []
        operators = Stack()

        i = 0
        while i < len(self.expression):
            char = self.expression[i]

            # If the character is a digit, handle multi-digit numbers
            if char.isdigit():
                num = char
                while i + 1 < len(self.expression) and self.expression[i + 1].isdigit():
                    i += 1
                    num += self.expression[i]
                output.append(num)

            # If the character is '(', push it to the operators stack
            elif char == '(':
                operators.push(char)

            # If the character is ')', pop and output from the stack until '(' is found
            elif char == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '(' from stack

            # If the character is an operator
            elif char in '+-*/':
                while (not operators.is_empty() and
                       self.precedence(operators.peek()) >= self.precedence(char)):
                    output.append(operators.pop())
                operators.push(char)

            i += 1

        # Pop all operators left in the stack
        while not operators.is_empty():
            output.append(operators.pop())

        return output

    def evaluate_postfix(self, postfix):
        """Evaluate a postfix expression."""
        operands = Stack()

        for char in postfix:
            if char.isdigit():
                operands.push(int(char))
            else:
                self.apply_operator(operands, char)

        return operands.pop()

    def evaluate(self):
        """Evaluate the infix expression."""
        postfix = self.to_postfix()
        return self.evaluate_postfix(postfix)



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





