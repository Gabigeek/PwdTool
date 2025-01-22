import unittest
from password import *

class check_fx_pwd_strength(unittest.TestCase):
    def test_very_weak(self):
        test_password= Password("1234")
        self.assertEqual(test_password.check_password_strength(), "Very_weak")

    def test_strong(self):
        test_password= Password("verysecurepassword!1234")
        self.assertEqual(test_password.check_password_strength(), "Strong")


if __name__ == "__main__":
    unittest.main()