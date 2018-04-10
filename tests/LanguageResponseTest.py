import unittest
import meaningcloud
import json


class LanguageResponseTest(unittest.TestCase):

    outputOK = {"status": {"code": "0", "msg": "OK", "credits": "1"}, "language_list":[{"language": "en", "relevance": 100, "name": "English", "iso639-3": "eng", "iso639-2": "en"}]}
    outputOK = json.dumps(outputOK)
    response = meaningcloud.LanguageResponse(outputOK)

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.LanguageResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.LanguageResponse('')


if __name__ == '__main__':
    unittest.main()
