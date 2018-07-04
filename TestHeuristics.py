import unittest
import EightPuzzleWithHeuristics as E
from AStar import isSolvable
import math as m

class TestHeuristics(unittest.TestCase):

    def test_h_hamming(self):
        a = E.State([[0,3,2],[1,7,4],[8,5,6]])
        self.assertTrue(a.h_hamming() == 7)
        b = E.State([[0,1,3],[4,6,7],[5,8,2]])
        self.assertTrue(b.h_hamming() == 7)
        c = E.State([[-2,-5,-6],[99,82,45],[99,17,56]])
        self.assertTrue(c.h_hamming() == 8)
        d = E.State([[0,1,2],[3,4,5],[6,7,8]])
        self.assertTrue(d.h_hamming() == 0)
        e = E.State(([[0,1,2],[4,3,5],[7,6,8]]))
        self.assertTrue(e.h_hamming() == 4)
        f = E.State([[3, 1, 2], [4, 5, 0], [6, 7, 8]])
        self.assertTrue(f.h_hamming() == 3)
        print("Hamming tests Passed!")

    def test_isSolvable(self):
        a = E.State([[3, 1, 2], [4,5,0], [6,7,8]])
        self.assertTrue(isSolvable(a))
        b = E.State([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        self.assertTrue(isSolvable(b))
        c = E.State([[0, 1, 2], [3, 4, 5], [6, 8, 7]])
        self.assertFalse(isSolvable(c))
        d = E.State([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue(isSolvable(d))
        e = E.State([[8, 7, 6], [5, 0, 3], [4, 2, 1]])
        self.assertFalse(isSolvable(e))
        print("tests passed")

    def test_h_manhattan(self):
        a = E.State([[3, 1, 2], [4, 5, 0], [6, 7, 8]])
        self.assertTrue(a.h_manhattan() == 3)
        b = E.State([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        self.assertTrue(b.h_manhattan() == 20)
        c = E.State([[7,2,4], [5, 0, 6], [8, 3, 1]])
        self.assertTrue(c.h_manhattan() == 18)
        print("Manhattan passes!")

    def test_h_euclidian(self):
        a = E.State([[8, 1, 2], [3, 4, 5], [6, 7, 0]])
        self.assertTrue(a.h_euclidian() == m.sqrt(8))
        b = E.State([[3, 1, 2], [4, 5, 0], [6, 7, 8]])
        self.assertTrue(b.h_euclidian() == 3)
        c = E.State(([[8, 7, 6], [5, 4, 3], [2, 1, 0]]))
        result = c.h_euclidian()
        #print(result)
        #self.assertTrue(c.h_euclidian() == 3*m.sqrt(8) + 8)

        print("Euclidian passes!")

    def test_custom(self):
        a = E.State([[0, 2, 1], [3, 7, 8], [4, 6, 5]])
        self.assertTrue(a.h_manhattan() == 8)
        self.assertTrue(a.h_custom() == 10)
        b = E.State([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        self.assertTrue(b.h_manhattan() == 20)
        self.assertTrue(b.h_custom() == 22)
        print("custom tests passed")

if __name__ == '__main__':
    unittest.main()