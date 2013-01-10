'''
Created on 2013-1-10

@author: xizhao
'''
import unittest
from Piece import *

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.blackpiece = Piece("B")
        self.wightpiece = Piece("W")
        
    def testInit(self):
        self.assertEqual('B', self.blackpiece.color)
        self.assertEqual('W', self.wightpiece.color)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()