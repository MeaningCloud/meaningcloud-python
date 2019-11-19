import unittest
import meaningcloud


class ClusteringRequestTest(unittest.TestCase):
    URL = 'https://api.meaningcloud.com/clustering-1.1'
    KEY = 'MY_KEY'
    TIMEOUT_DEFAULT = 60
    RESOURCES_DIR = './resources/'
    lang = 'en'
    texts = {'A01': 'London is big', 'A02': 'That city is fantastic'}
    mode = 'tm'
    request = meaningcloud.ClusteringRequest(KEY, lang=lang, texts=texts, mode=mode)

    def testConstruct(self):
        request = self.request
        self.assertEqual(self.URL, request.getUrl())
        self.assertIsNotNone(request.getParams())
        params = request.getParams()
        self.assertEqual('key' in params.keys(), True)
        self.assertEqual(params['key'], self.KEY)
        self.assertIsNotNone(request.getTimeout())
        self.assertEqual(self.TIMEOUT_DEFAULT, request.getTimeout())

        extraHeaders = ["Accept: application/json"]
        request2 = meaningcloud.ClusteringRequest(self.KEY, lang=self.lang, texts=self.texts, mode=self.mode, extraheaders=extraHeaders)
        self.assertIsNotNone(request2.sendReq())

        otherparams = {'key2': 'my_key2'}
        request3 = meaningcloud.ClusteringRequest(self.KEY, lang=self.lang, texts=self.texts, mode=self.mode, extraheaders=extraHeaders, otherparams=otherparams)
        self.assertIsNotNone('key2' in request3.getParams().keys(), True)
        self.assertEqual(request3.getParams()['key2'], 'my_key2')
        
        return request

    def testSendReq(self):
        request = self.request
        requestRq = request.sendReq()
        self.assertIsNotNone(requestRq)


if __name__ == '__main__':
    unittest.main()
