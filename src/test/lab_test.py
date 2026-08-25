import unittest

from src.main.user import User
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_delete(self):
        """
        In this test we are retrieving everything in the users table to ensure that Steve was successfully
        removed and comparing it to the hardcoded values below.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM site_user;")
            actual_result = [User(row[0], row[1]) for row in cur.fetchall()]
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        expected_result = [
            User(2, "Alexa"),
            User(4, "Brandon"),
            User(5, "Adam"),
        ]

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
