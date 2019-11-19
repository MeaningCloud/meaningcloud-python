import unittest
import meaningcloud
import json


class SummarizationResponseTest(unittest.TestCase):

    outputOK = {"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"32014"},"summary":"London is big."}
    outputOK = json.dumps(outputOK)
    response = meaningcloud.SummarizationResponse(outputOK)

    outputEmpty = {"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"32014"},"summary":""}
    empty_response = meaningcloud.SummarizationResponse(json.dumps(outputEmpty))

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.SummarizationResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.SummarizationResponse('')

    def testGetSummary(self):
        self.assertIsNotNone(self.response.getSummary())

    def testGetSummaryWithEmptyInput(self):
        self.assertEqual(self.empty_response.getSummary(), '')

if __name__ == '__main__':
    unittest.main()
