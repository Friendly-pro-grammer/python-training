import unittest
from unittest.mock import patch

from user import get_user_name


class TestUser(unittest.TestCase):

    @patch("user.requests.get")
    def test_get_user_name(self, mock_get):

       
        mock_get.return_value.json.return_value = {
            "name": "amit"
        }

        
        result = get_user_name(10)

        
        self.assertEqual(result, "amit")


if __name__ == "__main__":
    unittest.main()