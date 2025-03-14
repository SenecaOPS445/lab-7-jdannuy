#!/usr/bin/env python3
# Student ID: jdannuy

#!/usr/bin/env python3
import unittest

# Function to test
def function1():
    a = 'object_function1'
    return a  # Returning value for the test case

def function2():
    a = 'object_function2'
    return a  # Returning value for the test case

# Test case class
class TestLab7G(unittest.TestCase):

    def test_function1(self):
        # Test the output of function1
        result = function1()
        self.assertEqual(result, 'object_function1')  # Check if it returns the expected value

    def test_function2(self):
        # Test the output of function2
        result = function2()
        self.assertEqual(result, 'object_function2')  # Check if it returns the expected value

if __name__ == '__main__':
    unittest.main()
