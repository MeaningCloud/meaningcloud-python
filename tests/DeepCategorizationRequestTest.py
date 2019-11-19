import unittest
import meaningcloud


class DeepCategorizationRequestTest(unittest.TestCase):
    URL = 'https://api.meaningcloud.com/deepcategorization-1.0'
    KEY = 'MY_KEY'
    TIMEOUT_DEFAULT = 60
    RESOURCES_DIR = './resources/'
    text = 'London is big'
    model = 'IAB_2.0_en'
    polarity = 'n'
    request = meaningcloud.DeepCategorizationRequest(KEY, model=model, txt=text, polarity=polarity)

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
        request2 = meaningcloud.DeepCategorizationRequest(self.KEY, model=self.model, txt=self.text, polarity=self.polarity, extraheaders=extraHeaders)
        self.assertIsNotNone(request2.sendReq())

        otherparams = {'key2': 'my_key2'}
        request3 = meaningcloud.DeepCategorizationRequest(self.KEY, model=self.model, txt=self.text, polarity=self.polarity, extraheaders=extraHeaders,
                                             otherparams=otherparams)
        self.assertIsNotNone('key2' in request3.getParams().keys(), True)
        self.assertEqual(request3.getParams()['key2'], 'my_key2')

        url = 'https://en.wikipedia.org/wiki/Star_Trek'
        request4 = meaningcloud.DeepCategorizationRequest(self.KEY, model=self.model, url=url, polarity=self.polarity, extraheaders=extraHeaders,
                                             otherparams=otherparams)

        self.assertIsNotNone('url' in request4.getParams().keys(), True)
        self.assertEqual(request4.getParams()['url'], url)

        file = self.RESOURCES_DIR + 'file.txt'
        request5 = meaningcloud.DeepCategorizationRequest(self.KEY, model=self.model, doc=file, polarity=self.polarity, extraheaders=extraHeaders,
                                             otherparams=otherparams)

        self.assertIsNotNone('doc' in request5.getParams().keys(), False)
        doc = request5._file['doc'].read().decode('utf-8')

        request5._file['doc'].close()
        aux_doc = open(self.RESOURCES_DIR + 'file.txt', 'rb')
        aux_content = aux_doc.read().decode('utf-8')
        aux_doc.close()
        self.assertEqual(aux_content, doc)

        return request

    def testSendReq(self):
        request = self.request
        requestRq = request.sendReq()
        self.assertIsNotNone(requestRq)


if __name__ == '__main__':
    unittest.main()
