import unittest
import meaningcloud
import json


class LanguageResponseTest(unittest.TestCase):

    outputOK = {"status": {"code": "0", "msg": "OK", "credits": "1", "remaining_credits": "32033"}, "language_list":[{"language": "en", "relevance": 100, "name": "English", "iso639-3": "eng", "iso639-2": "en"}]}
    outputOK = json.dumps(outputOK)
    response = meaningcloud.LanguageResponse(outputOK)

    outputEmpty = {"status": {"code": "0", "msg": "OK", "credits": "1", "remaining_credits": "32033"}, 'language_list': []}
    empty_response = meaningcloud.LanguageResponse(json.dumps(outputEmpty))

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.LanguageResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.LanguageResponse('')

    def testGetLanguages(self):
        self.assertIsNotNone(self.response.getLanguages())
        self.assertTrue(isinstance(self.response.getLanguages(), list))

    def testGetNonexistentLanguages(self):
        self.assertEqual(len(self.empty_response.getLanguages()), 0)

    def testGetLanguageCode(self):
        languages = self.response.getLanguages()
        language = languages[0] if((len(languages) > 0) and (languages[0] is not None)) else []
        self.assertIsNotNone(self.response.getLanguageCode(language))

    def testGetLanguageCodeWithEmptyInput(self):
        self.assertEqual(self.response.getLanguageCode([]), "")

    def testGetLanguageName(self):
        languages = self.response.getLanguages()
        language = languages[0] if ((len(languages) > 0) and (languages[0] is not None)) else []
        self.assertIsNotNone(self.response.getLanguageName(language))

    def testGetLanguageNameWithEmptyInput(self):
        self.assertEqual(self.response.getLanguageName([]), "")

if __name__ == '__main__':
    unittest.main()
