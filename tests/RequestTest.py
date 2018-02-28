import meaningcloud
import unittest

class RequestTest(unittest.TestCase):
    URL = 'https://api.meaningcloud.com/topics-2.0'
    KEY = 'MY_KEY'
    TIMEOUT_DEFAULT = 60
    RESOURCES_DIR = './resources/'
    request = meaningcloud.Request(URL, KEY)

    def testConstruct(self):
        request = self.request
        self.assertEqual(self.URL, request.getUrl())
        self.assertIsNotNone(request.getParams())
        params = request.getParams()
        self.assertEqual('key' in params.keys(),True)
        self.assertEqual(params['key'],self.KEY)
        self.assertIsNotNone(request.getTimeout())
        self.assertEqual(self.TIMEOUT_DEFAULT, request.getTimeout())
        return request

    def testConstructWithEmpyParams(self):
        with self.assertRaises(ValueError):
            meaningcloud.Request('','')
        with self.assertRaises(ValueError):
            meaningcloud.Request(self.URL, '')
        with self.assertRaises(ValueError):
            meaningcloud.Request('', self.KEY)


    def testAddParam(self):
        request = self.request
        request.addParam('lang','en')
        params = request.getParams()
        self.assertEqual('lang' in params.keys(), True)
        self.assertEqual('en',params['lang'])

        request.addParam('of', 'json')
        params = request.getParams()
        self.assertEqual('of' in params.keys(), True)
        self.assertEqual('json', params['of'])

    def testAddParamWithEmptyName(self):
        request = self.request
        with self.assertRaises(ValueError):
            request.addParam('','en')

    def testSetContentTxt(self):
        request = self.request
        txt= 'This is MeaningCloud\'s official Python client'
        request.setContentTxt(txt)
        params = request.getParams()
        self.assertEqual('txt' in params.keys(), True)
        self.assertEqual(txt, params['txt'])


    def testSetContentUrl(self):
        request = self.request
        url= 'https://en.wikipedia.org/wiki/Star_Trek'
        request.setContentUrl(url)
        params = request.getParams()
        self.assertEqual('url' in params.keys(), True)
        self.assertEqual(url, params['url'])


    def testSetContentFile(self):
        file = self.RESOURCES_DIR+'file.txt'
        self.request.setContentFile(file)
        params = self.request.getParams()
        self.assertTrue('doc' in params.keys())
        self.assertIsNotNone(params['doc'].name)
        doc = params['doc'].readlines()
        params['doc'].close()
        aux_doc = open(self.RESOURCES_DIR+'file.txt','rb')
        aux_conten = aux_doc.readlines()
        aux_doc.close()
        self.assertEqual(aux_conten,doc)

    def testSetTimeout(self):
        timeout = 360
        request = self.request
        request.setTimeout(timeout)
        self.assertEqual(timeout, request.getTimeout())

    def testSendRequest(self):
        request = self.request
        strResponse = request.sendRequest()
        response = meaningcloud.Response(strResponse)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.getResponse())

    def testSendReqExtraHeaders(self):
        request = self.request
        extraHeaders = ["Accept: application/json"]
        strResponse = request.sendRequest(extraHeaders)
        response = meaningcloud.Response(strResponse)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.getResponse())

    def testSetURL(self):
        url = 'https://myinstance.meaningcloud.com'
        request = self.request
        request.setUrl(url)
        self.assertEqual(url, request.getUrl())






if __name__ == '__main__':
    unittest.main()
