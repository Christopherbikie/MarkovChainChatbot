import unittest


def remChars(string, chars):
    return string.translate({ord(c): None for c in chars})


class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(remChars("this is a test", "."), "this is a test")
        self.assertEqual(remChars("this is a test.", "."), "this is a test")
        self.assertEqual(remChars("this is a test", ""), "this is a test")
        self.assertEqual(remChars("1t2h3i4s5 i6s a t7e8s9t0", "5781962403"), "this is a test")
