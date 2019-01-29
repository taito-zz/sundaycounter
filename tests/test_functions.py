import unittest


class TestCase(unittest.TestCase):
    """TestCase for class: sundaycounter.SundayCounter"""

    def test_new_sunday(self):
        from sundaycounter import new_sunday
        self.assertEqual(new_sunday((1900, 1, 1)), (1900, 1, 7))
        self.assertEqual(new_sunday((1900, 1, 2)), (1900, 1, 7))
        self.assertEqual(new_sunday((1900, 1, 6)), (1900, 1, 7))
        self.assertEqual(new_sunday((1900, 1, 7)), (1900, 1, 14))
        self.assertEqual(new_sunday((1900, 1, 14)), (1900, 1, 21))
        self.assertEqual(new_sunday((1900, 1, 21)), (1900, 1, 28))
        self.assertEqual(new_sunday((1900, 1, 28)), (1900, 2, 4))
        self.assertEqual(new_sunday((1900, 2, 4)), (1900, 2, 11))
        self.assertEqual(new_sunday((1900, 2, 11)), (1900, 2, 18))
        self.assertEqual(new_sunday((1900, 2, 18)), (1900, 2, 25))
        self.assertEqual(new_sunday((1900, 2, 27)), (1900, 3, 4))
        self.assertEqual(new_sunday((1900, 12, 29)), (1900, 12, 30))
        self.assertEqual(new_sunday((1900, 12, 30)), (1901, 1, 6))

    def test_int_date(self):
        from sundaycounter import int_date
        self.assertEqual(int_date('1.2.1900'), (1900, 2, 1))

    def test_list_sundays(self):
        from sundaycounter import list_sundays
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 1)), [])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 2)), [])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 6)), [])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 7)), [])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 8)), ['7.1.1900'])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 14)), ['7.1.1900'])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 1, 20)), ['7.1.1900', '14.1.1900'])
        self.assertEqual(list_sundays((1900, 1, 1), (1900, 2, 5), reverse=True), [
                '4.2.1900', '28.1.1900', '21.1.1900', '14.1.1900', '7.1.1900'])
        self.assertEqual(list_sundays((1900, 12, 28), (1901, 1, 15)), ['30.12.1900', '6.1.1901', '13.1.1901'])
