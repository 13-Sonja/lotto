import unittest
from unittest.mock import patch
from io import StringIO
from random import sample
from silvester import play_silvester, drawing, calculate_winnings, input_validation


class SilvesterGameTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["5"])
    def test_play_silvester(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            play_silvester()
            output = fake_output.getvalue()
            self.assertIn("Euro gekauft", output)
            self.assertIn("Euro gewonnen", output)

    def test_input_validation_invalid_input(self):
        txt = "abc"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = input_validation(txt)
            self.assertEqual(
                fake_output.getvalue().strip(),
                "Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 1750000 eingeben.",
            )

    def test_input_validation_invalid_amount(self):
        txt = "0"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = input_validation(txt)
            self.assertEqual(
                fake_output.getvalue().strip(),
                "Ungültige Anzahl. Bitte eine Zahl zwischen 1 und 1750000 eingeben.",
            )

    def test_drawing(self):
        TICKETS = list(range(1, 1750001))
        class_1 = sample(TICKETS, 7)
        self.assertEqual(len(class_1), 7)
        for ticket in class_1:
            TICKETS.pop(ticket)
        class_2 = sample(TICKETS, 7)
        self.assertEqual(len(class_2), 7)
        section = list(set(class_2).intersection(class_1))
        self.assertEqual(len(section), 0)
        for ticket in class_2:
            TICKETS.pop(ticket)
        class_3 = sample(TICKETS, 1750)
        self.assertEqual(len(class_3), 1750)
        section = list(set(class_3).intersection(class_1 + class_2))
        self.assertEqual(len(section), 0)

    def test_calculate_winnings_no_winnings(self):
        draws = (
            (1, 10, 111, 2222, 33333, 444444, 1750000),
            (2, 11, 222, 3333, 44444, 555555, 1749999),
            (),
            (1, 10, 22, 33, 44, 55),
        )
        my_tickets = (123456, 777)
        self.assertEqual(calculate_winnings(draws, my_tickets), 0)

    def test_calculate_winnings_two_winnings(self):
        draws = (
            (1, 10, 111, 2222, 33333, 444444, 1750000),
            (2, 11, 222, 3333, 44444, 555555, 1749999),
            (),
            (1, 10, 22, 33, 44, 55),
        )
        my_tickets = (444444, 777)
        self.assertEqual(calculate_winnings(draws, my_tickets), 1000010)


if __name__ == "__main__":
    unittest.main()
