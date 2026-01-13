import unittest

from src.helpers.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_error(self):
        with self.assertRaises(Exception) as context:
            extract_title("> Hola mundo")

        self.assertEqual(
            str(context.exception),
            "Header not found. Please ensure a header is present in the content.",
        )

    def test_extract_title(self):
        text = extract_title("# Hola mundo")
        expected = "Hola mundo"
        self.assertEqual(text, expected)

    def test_extract_title_with_spaces(self):
        text = extract_title("  # Hola mundo  ")
        expected = "Hola mundo"
        self.assertEqual(text, expected)


if __name__ == "__main__":
    unittest.main()
