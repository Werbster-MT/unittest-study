import unittest
from library.pilot import Pilot

class TestPilot(unittest.TestCase):
    def setUp(self):
        self.pilot1 = Pilot('Steve', 'Jobs', 2000)
        self.pilot2 = Pilot('Pedro', 'Sampaio', 2000)
        self.pilot3 = Pilot('Joao', 'Lucas', 500)

    def test_email(self):
        self.assertEqual(self.pilot1.email, 'Steve.Jobs@email.com')
        self.assertEqual(self.pilot2.email, 'Pedro.Sampaio@email.com')
        self.assertEqual(self.pilot3.email, 'Joao.Lucas@email.com')

    def test_full_name(self):
        self.assertEqual(self.pilot1.full_name, 'Steve Jobs')
        self.assertEqual(self.pilot2.full_name, 'Pedro Sampaio')
        self.assertEqual(self.pilot3.full_name, 'Joao Lucas')

    def test_increase_salary(self):
        self.assertEqual(self.pilot1.increase_salary(), 2000 + (2000 * 1.10))
        self.assertEqual(self.pilot2.increase_salary(), 2000 + (2000 * 1.10))
        self.assertEqual(self.pilot3.increase_salary(), 500 + (500 * 1.10))


if __name__ == '__main__':
    unittest.main()
