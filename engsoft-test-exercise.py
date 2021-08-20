# run command
# python -m unittest -v engsoft-test-exercise.py

import unittest


class EngSoftTest(unittest.TestCase):

    def test_is_empty(self):
        self.assertFalse(is_empty([1, 2, 3]), False)
        self.assertTrue(is_empty([]), True)

    def test_reverse(self):
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse([]), [])

    def test_bissexto(self):
        self.assertTrue(bissexto(2020), True)
        self.assertTrue(bissexto(2000), True)
        self.assertFalse(bissexto(2009), False)
        self.assertFalse(bissexto(1965), False)


def is_empty(lista):
    return not len(lista) > 0


def reverse(lista):
    return lista[::-1]


def bissexto(ano):
    if not ano % 4 and (ano % 100 or not ano % 400):
        return True
    return False


if __name__ == "__main__":
    unittest.main()
