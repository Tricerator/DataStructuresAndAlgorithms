from bubbleSort import bubbleSort
import unittest


class TestSum(unittest.TestCase):

    def test_bubbleSort(self):
        self.assertEqual([1, 2, 3], bubbleSort([3,2,1]))
        self.assertEqual([0,0,0,0,0, 1, 2, 3], bubbleSort([3,2,1,0,0,0,0,0]))


if __name__ == '__main__':
    unittest.main()
