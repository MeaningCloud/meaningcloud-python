import unittest
import meaningcloud


class LanguageRequestTest(unittest.TestCase):
    URL = 'https://api.meaningcloud.com/lang-2.0'
    KEY = 'MY_KEY'
    TIMEOUT_DEFAULT = 60
    RESOURCES_DIR = './resources/'
    text = 'London is big'

    request = meaningcloud.LanguageRequest(KEY, txt=text)

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
        request2 = meaningcloud.LanguageRequest(self.KEY, txt=self.text, extraheaders=extraHeaders)
        self.assertIsNotNone(request2.sendReq())

        otherparams = {'key2': 'my_key2'}
        request3 = meaningcloud.LanguageRequest(self.KEY, txt=self.text, extraheaders=extraHeaders,
                                                otherparams=otherparams)
        self.assertIsNotNone('key2' in request3.getParams().keys(), True)
        self.assertEqual(request3.getParams()['key2'], 'my_key2')

        url = 'https://en.wikipedia.org/wiki/Star_Trek'
        request4 = meaningcloud.LanguageRequest(self.KEY, url=url, extraheaders=extraHeaders, otherparams=otherparams)
        self.assertIsNotNone('url' in request4.getParams().keys(), True)
        self.assertEqual(request4.getParams()['url'], url)

        file = self.RESOURCES_DIR + 'file.txt'
        request5 = meaningcloud.LanguageRequest(self.KEY, doc=file, extraheaders=extraHeaders,
                                                otherparams=otherparams)

        self.assertIsNotNone('doc' in request5.getParams().keys(), False)
        doc = request5._file['doc'].read().decode('utf-8')

        request5._file['doc'].close()
        aux_doc = open(self.RESOURCES_DIR + 'file.txt', 'rb')
        aux_conten = aux_doc.read().decode('utf-8')
        aux_doc.close()
        self.assertEqual(aux_conten, doc)

        return request

    def testSendReq(self):
        request = self.request
        requestRq = request.sendReq()
        self.assertIsNotNone(requestRq)


if __name__ == '__main__':
    unittest.main()
