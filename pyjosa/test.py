from jonsung import is_hangle, has_jongsung
import unittest

class HangleTestCase(unittest.TestCase):

    def setUp(self):
        self.kor = [ 
         '한글',
         '안녕',
         '하윙',
         '테스트케이스',
         'enflish영어'
        ]
        self.not_kor = [
            'english',
            '영어eng',
            '132r4eng',
            'dinvf,5'
        ]

    def test_line_count(self):
        for v in self.kor:
            self.assertTrue(is_hangle(v))
        
        for v in self.not_kor:
            self.assertFalse(is_hangle(v))

if __name__ == '__main__':
    unittest.main()