import unittest
from library.company import get_country

class TestCompany(unittest.TestCase):
    # Test Case: Allow Country
    def test_allow_country(self):
        iso_code_list = ['DK', 'DE', 'UK', 'SE', 'NO']

        for code in iso_code_list:
            country = get_country(iso_code=code)
            self.assertTrue(country[0])
            self.assertEqual(dict, type(country[1]))


    def test_disallow_country(self):
        # Test Case: Disallow Country
        country = get_country(iso_code='DA')
        self.assertFalse(country[0])
        self.assertEqual(None, country[1])


    def test_raise_country_type_error(self):
        # Exception Typer Errors
        with self.assertRaises(TypeError):
            get_country(iso_code=12)
            get_country(iso_code=12.00)
            get_country(True)
            get_country([])
            get_country({})
            get_country()

    def test_raise_country_value_error(self):
        # Exception Value Errors
        with self.assertRaises(ValueError):
            get_country(iso_code='Denmark')
            get_country(iso_code='D')
            get_country(iso_code='')


if __name__ == "__main__":
    unittest.main()
