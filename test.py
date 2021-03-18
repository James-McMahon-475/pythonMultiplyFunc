from mul import multiply
import unittest

class TestMethods(unittest.TestCase):

    def test_NaN_pass(self):
        out, error = multiply("a","b")
        assert out == "NaN"
        assert error == "true"

    def test_mul_pass(self):
        out, error = multiply(5, 2)
        assert out == 10
        assert error == "false"

    def test_zero_pass(self):
        out, error = multiply(1, 0)
        assert out == 0
        assert error == "false"

    @unittest.expectedFailure
    def test_NaN_fail(self):
        out, error = multiply(5,2)
        assert out == "NaN"
        assert error == "true"

    @unittest.expectedFailure
    def test_mul_fail(self):
        out, error = multiply("a","b")
        assert out == 1
        assert error == "false"

    @unittest.expectedFailure
    def test_zero_fail(self):
        out, error = multiply(0, 0)
        assert out == 0
        assert error == "true"

if __name__ == '__main__':
    unittest.main()