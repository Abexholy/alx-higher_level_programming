#!/usr/bin/python3
class MyInt(int):
    """Class  from class int"""

    def __eq__(self, other):
        """Operator to check behavior in checks"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Operartor with the == check"""
        return int.__eq__(self, other)
