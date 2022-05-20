import unittest

from unittest.mock import Mock

import datetime

def is_weak_day():
    today = datetime.datetime.today()
    # 0 is monday and 6 is sunday
    if 0 <= today.weekday() < 5:
        return "Dia da semana: True"

    return "Fim de semana: True"

class TestCalendary(unittest.TestCase):
    def setUp(self) -> None:
        self.datetime = Mock()

        self.friday = self.datetime.datetime(year=2022, month=5, is_weak_day=20)
        self.saturday = self.datetime.datetime(year=2022, month=5, is_weak_day=21)

        self.datetime.today.return_value = self.saturday

    #def test_is_weak_day(self):
        #self.datetime.today.return_value = self.friday
        #self.assertEqual(is_weak_day(), "Dia da semana: True")

    def test_is_not_weak_day(self):
        #self.datetime.today.return_value = self.saturday
        self.assertEqual(is_weak_day(), "Fim de semana: True")

if __name__ == '__main__':
    unittest.main()
