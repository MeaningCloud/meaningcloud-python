import unittest
import meaningcloud
import json


class SentimentResponseTest(unittest.TestCase):

    outputOK = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"model":"general_en","score_tag":"P+","agreement":"AGREEMENT","subjectivity":"SUBJECTIVE","confidence":"98","irony":"NONIRONIC","sentence_list":[{"text":"Main dishes were quite good, but desserts were too sweet for me.","inip":"0","endp":"65","bop":"y","confidence":"98","score_tag":"P+","agreement":"AGREEMENT","segment_list":[{"text":"Main dishes were quite good","segment_type":"main","inip":"0","endp":"27","confidence":"98","score_tag":"P+","agreement":"AGREEMENT","polarity_term_list":[{"text":"(quite) good","inip":"24","endp":"27","confidence":"98","score_tag":"P+"}]},{"text":"desserts were too sweet for me","segment_type":"main","inip":"34","endp":"63","confidence":"100","score_tag":"P","agreement":"AGREEMENT","polarity_term_list":[{"text":"sweet@A","inip":"52","endp":"56","confidence":"100","score_tag":"P","sentimented_concept_list":[{"form":"dessert","id":"0e15bbd941","variant":"desserts","inip":"34","endp":"41","type":"Top>Product>Food","score_tag":"P"}]}]},{"text":"","segment_type":"secondary","inip":"65","endp":"65","confidence":"100","score_tag":"NONE","agreement":"AGREEMENT","polarity_term_list":[],"sentimented_concept_list":[{"form":"dessert","id":"0e15bbd941","variant":"desserts","inip":"34","endp":"41","type":"Top>Product>Food","score_tag":"NONE"}]}],"sentimented_entity_list":[],"sentimented_concept_list":[{"form":"dessert","id":"0e15bbd941","type":"Top>Product>Food","score_tag":"P"}]}],"sentimented_entity_list":[],"sentimented_concept_list":[{"form":"dessert","id":"0e15bbd941","type":"Top>Product>Food","score_tag":"P"}]}'
    response = meaningcloud.SentimentResponse(outputOK)
    outputEmpty = '{"status": {"code": "0","msg": "OK","credits": "1","remaining_credits":"5000"}}'
    empty_response = meaningcloud.SentimentResponse(outputEmpty)

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.SentimentResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.SentimentResponse('')

    def testConstructEmptyResult(self):
        self.assertIsNotNone(self.empty_response.getResponse())

    def testGetGlobalModel(self):
        self.assertIsNotNone(self.response.getModel())

    def testGetGlobalModelWithEmptyInput(self):
        self.assertEqual(self.empty_response.getModel(), '')

    def testGetGlobalScoreTag(self):
        self.assertIsNotNone(self.response.getGlobalScoreTag())

    def testGetGlobalScoreTagWithEmptyInput(self):
        self.assertEqual(self.empty_response.getGlobalScoreTag(), '')

    def testGetGlobalAgreement(self):
        self.assertIsNotNone(self.response.getGlobalAgreement())

    def testGetGlobalAgreementWithEmptyInput(self):
        self.assertEqual(self.empty_response.getGlobalAgreement(), '')

    def testGetAgreement(self):
        sentence_list = self.response.getResponse()['sentence_list']
        self.assertIsNotNone(self.response.getAgreement(sentence_list[0]))

    def testGetAgreementWithEmptyInput(self):
        with self.assertRaises(AttributeError):
            self.empty_response.getAgreement([])

    def testGetGlobalSubjectivity(self):
        self.assertIsNotNone(self.response.getSubjectivity())

    def testGetGlobalSubjectivityWithEmptyInput(self):
        self.assertIsNotNone(self.empty_response.getSubjectivity())

    def testGetGlobalConfidence(self):
        self.assertIsNotNone(self.response.getGlobalConfidence())

    def testGetGlobalConfidenceWithEmptyInput(self):
        self.assertIsNotNone(self.empty_response.getGlobalConfidence())

    def testGetConfidence(self):
        sentence_list = self.response.getResponse()['sentence_list']
        self.assertIsNotNone(self.response.getConfidence(sentence_list[0]))

    def testGetConfidenceWithEmptyInput(self):
        with self.assertRaises(AttributeError):
            self.empty_response.getAgreement([])

    def testGetGlobalIrony(self):
        self.assertIsNotNone(self.response.getIrony())

    def testGetGlobalIronyWithEmptyInput(self):
        self.assertIsNotNone(self.empty_response.getIrony())

    def testGetGlobalSentimentedEntities(self):
        self.assertEqual(isinstance(self.response.getGlobalSentimentedEntities(), list), True)

    def testGetGlobalSentimentedEntitiesWithEmptyInput(self):
        self.assertEqual(self.empty_response.getGlobalSentimentedEntities(), '')

    def testGetSentimentedEntities(self):
        sentence_list = self.response.getResponse()['sentence_list']
        self.assertEqual(isinstance(self.response.getSentimentedEntities(sentence_list[0]), list), True)

    def testGetSentimentedEntitiesWithEmptyInput(self):
        self.assertEqual(self.empty_response.getSentimentedEntities([]), '')

    def testGetGlobalSentimentedConcepts(self):
        self.assertEqual(isinstance(self.response.getGlobalSentimentedConcepts(), list), True)

    def testGetGlobalSentimentedConceptsWithEmptyInput(self):
        self.assertEqual(self.empty_response.getGlobalSentimentedConcepts(), '')

    def testGetSentimentedConcepts(self):
        sentence_list = self.response.getResponse()['sentence_list']
        self.assertEqual(isinstance(self.response.getSentimentedConcepts(sentence_list[0]), list), True)

    def testGetSentimentedConceptsWithEmptyInput(self):
        self.assertEqual(self.empty_response.getSentimentedConcepts([]), '')

    def testScoreTagToString(self):
        d = {'P+': 'strong positive', 'P': 'positive', 'NEU': 'neutral', 'N': 'negative',
             'N+': 'strong negative', 'NONE': 'no sentiment'}
        for x in d.items():
            self.assertEqual(x[1], self.response.scoreTagToString(x[0]))


if __name__ == '__main__':
    unittest.main()
