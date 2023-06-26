import unittest
from io import StringIO
from unittest.mock import patch
from random import sample, choice
from lotto import play_lotto, drawing, calculate_winnings, input_validation


class LottoGameTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["5", "3"])
    def test_play_lotto(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            play_lotto()
            output = fake_output.getvalue()
            self.assertIn("Ziehung 1", output)
            self.assertIn("Ziehung 2", output)
            self.assertIn("Ziehung 3", output)
            self.assertIn("Kosten gesamt", output)
            self.assertIn("Gewinn gesamt", output)

    def test_drawing(self):
        NORMAL_NUMBERS = list(range(1, 50))
        SUPERNUMBER = list(range(0, 10))
        drawn_numbers, drawn_supernumber = drawing(NORMAL_NUMBERS, SUPERNUMBER)
        self.assertEqual(len(drawn_numbers), 6)
        self.assertIn(drawn_supernumber, SUPERNUMBER)

    def test_calculate_winnings_no_winning_tickets(self):
        my_tickets = [([1, 2, 3, 4, 5, 6], 0), ([7, 8, 9, 10, 11, 12], 1)]
        winning_nums = ([13, 14, 15, 16, 17, 18], 2)
        winnings = calculate_winnings(my_tickets, winning_nums)
        self.assertEqual(winnings, 0)

    def test_calculate_winnings_one_winning_ticket(self):
        my_tickets = [
            ([1, 2, 3, 4, 5, 6], 0),
            ([7, 8, 9, 10, 11, 12], 1),
        ]
        winning_nums = ([1, 2, 3, 4, 5, 6], 0)
        winnings = calculate_winnings(my_tickets, winning_nums)
        self.assertEqual(winnings, 9000000)

    def test_calculate_winnings_two_winning_ticket(self):
        my_tickets = [
            ([1, 2, 3, 4, 5, 31], 1),
            ([1, 2, 3, 33, 34, 35], 0),
        ]
        winning_nums = ([1, 2, 3, 4, 5, 6], 0)
        winnings = calculate_winnings(my_tickets, winning_nums)
        self.assertEqual(winnings, 3321)

    def test_input_validation_valid_input(self):
        txt = "5"
        max_amount = 10
        result = input_validation(txt, max_amount)
        self.assertEqual(result, 5)

    def test_input_validation_invalid_input(self):
        txt = "abc"
        max_amount = 10
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = input_validation(txt, max_amount)
            self.assertFalse(result)
            self.assertEqual(
                fake_output.getvalue().strip(),
                "Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 10 eingeben.",
            )

    def test_input_validation_invalid_amount(self):
        txt = "15"
        max_amount = 10
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = input_validation(txt, max_amount)
            self.assertFalse(result)
            self.assertEqual(
                fake_output.getvalue().strip(),
                "Ungültige Anzahl. Bitte eine Zahl zwischen 1 und 10 eingeben.",
            )


if __name__ == "__main__":
    unittest.main()
