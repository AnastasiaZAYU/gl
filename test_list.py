import unittest


def swap_the_first_elements(list):
    list[0], list[1] = list[1], list[0]
    return list


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_michael_medved_fi93(self):
        self.assertEqual(len([] + ['f']), len('f'))

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2 * [1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_kostiantyn_baievskyi_fi_93(self):
        self.assertEqual([1, 2, 3] + [4, 5, 6], [1, 2, 3, 4, 5, 6])

    def test_Anastasia_Zatsarenko_FI94(self):
        list1 = [2, 1, 3, 4, 5]
        list1 = swap_the_first_elements(list1)
        self.assertEqual(list1, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
