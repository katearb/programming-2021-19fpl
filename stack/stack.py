"""

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """

    def __init__(self, data: Iterable = None):
        self.data = list(data) if data is not None else []

    def __str__(self):
        """
        return string representation of the object
        """
        str_repr = ''
        while self.data:
            str_repr += self.top()
            self.pop()
        return str_repr

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        self.data.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        if not self.data:
            raise ValueError
        self.data.pop()

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        if self.data:
            return self.data[-1]
        raise ValueError

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.data)

    def print(self):
        """
        Print elements one by one in a column
        """
        for item in str(self):
            print(item)

    def clean_stack(self):
        """
        delete all elements
        """
        self.data = []
