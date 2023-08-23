import unittest
from library_of_babel import LoB

class LoBTest(unittest.TestCase):

    def test_a(self):
        self.lob = LoB()
        self.assertEqual(self.lob.stringToNumber('a'), 0)
        self.assertEqual(self.lob.stringToNumber('ba'), 29)

    def test_b(self):
        self.lob = LoB()
        self.assertEqual(len(self.lob.getPage('asaskjkfsdf:2:2:2:33')), self.lob.length_of_page)
        self.assertEqual('hello kitty', self.lob.toText(int(self.lob.int2base(self.lob.stringToNumber('hello kitty'), 36), 36)))

    def test_c(self):
        self.lob = LoB()
        self.assertEqual(self.lob.int2base(4, 36), '4')
        self.assertEqual(self.lob.int2base(10, 36), 'A')

    def test_d(self):
        self.lob = LoB()
        test_string = '.................................................'
        self.assertIn(test_string, self.lob.getPage(self.lob.search(test_string)))

    def test_e(self):
        self.lob = LoB()
        print('')
        self.lob.printPage('HELLO:0:0:0:0')

if __name__ == '__main__':
    unittest.main()
