import unittest
import meaningcloud

class ClassRequestTest(unittest.TestCase):
    URL = 'http://api.meaningcloud.com/class-1.1'
    KEY = 'MY_KEY'
    TIMEOUT_DEFAULT = 60
    RESOURCES_DIR = './resources/'
    text = 'London is big'
    model = 'IAB_en'
    request = meaningcloud.ClassRequest(KEY, txt=text, model=model)


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
        request2 = meaningcloud.ClassRequest(self.KEY, txt=self.text, model=self.model, extraheaders=extraHeaders)
        self.assertIsNotNone(request2.sendReq())

        otherparams = {'key2':'my_key2'}
        request3 = meaningcloud.ClassRequest(self.KEY, txt=self.text, model=self.model, extraheaders=extraHeaders,otherparams=otherparams)
        self.assertIsNotNone('key2' in request3.getParams().keys(), True)
        self.assertEqual(request3.getParams()['key2'],'my_key2')

        url = 'https://en.wikipedia.org/wiki/Star_Trek'
        request4 = meaningcloud.ClassRequest(self.KEY, url=url, model=self.model, extraheaders=extraHeaders,otherparams=otherparams)

        self.assertIsNotNone('url' in request4.getParams().keys(), True)
        self.assertEqual(request4.getParams()['url'], url)

        file = self.RESOURCES_DIR + 'file.txt'
        request5 = meaningcloud.ClassRequest(self.KEY, doc=file, model=self.model, extraheaders=extraHeaders,
                                              otherparams=otherparams)

        self.assertIsNotNone('doc' in request5.getParams().keys(), True)
        doc = request5.getParams()['doc'].readlines()
        request5.getParams()['doc'].close()
        aux_doc = open(self.RESOURCES_DIR + 'file.txt', 'rb')
        aux_conten = aux_doc.readlines()
        aux_doc.close()
        self.assertEqual(aux_conten, doc)

        return request

    def testSendReq(self):
        request = self.request
        requestRq = request.sendReq()
        self.assertIsNotNone(requestRq)



if __name__ == '__main__':
    unittest.main()
