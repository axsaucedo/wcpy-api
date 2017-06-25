import unittest, requests

class TestWCTextResource(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:3000/raw_text"

    def test_simple_text_request(self):
        test_data = {
            "sorted_list": False,
            "raw_text": """One two
                            Two Threes Threes
                            Threes Fives
                            and Fives
                            and Fives"""
        }
        response = requests.post(self.url, json=test_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["one"]["word_count"], 1)
        self.assertEqual(data["two"]["word_count"], 2)
        self.assertEqual(data["threes"]["word_count"], 3)
        self.assertEqual(data["fives"]["word_count"], 3)
        self.assertEqual(data["and"]["word_count"], 2)

    def test_simple_text_list_request(self):
        test_data = {
            "sorted_list": True,
            "raw_text": """One two
                            Two Threes Threes
                            Threes Fives
                            and Fives
                            and Fives"""
        }
        response = requests.post(self.url, json=test_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0]["word_count"], 3)
        self.assertEqual(data[1]["word_count"], 3)
        self.assertEqual(data[2]["word_count"], 2)
        self.assertEqual(data[3]["word_count"], 2)
        self.assertEqual(data[4]["word_count"], 1)

    def test_simple_empty_request(self):
        test_data = {}
        response = requests.post(self.url, json=test_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["error"], True)

