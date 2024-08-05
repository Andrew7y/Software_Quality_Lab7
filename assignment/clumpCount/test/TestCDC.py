# 653380120-2 sec.1 กัมแพงเพชร สิงห์ขรณ์

import unittest
import source.CountClump as C


class TestCDC(unittest.TestCase):
    def setUp(self):
        self.countClump = C.CountClump
        testName = self.shortDescription()

    def tearDown(self):
        print("\nEnd test : ", self.shortDescription())

    def testNoneAndEmptyList(self):
        """TC1 and TC2"""
        self.assertEqual(0, self.countClump.count_clumps(None))
        self.assertEqual(0, self.countClump.count_clumps([]))

    def testValidInput(self):
        """TC3 and TC4"""
        self.assertEqual(1, self.countClump.count_clumps([2, 2, 2, 1]))
        self.assertEqual(0, self.countClump.count_clumps([2, 1]))

    def makeSuite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestCDC("testNoneAndEmptyList"))
        suite.addTest(TestCDC("testValidInput"))
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    testSuite = TestCDC()
    runner.run(testSuite)
